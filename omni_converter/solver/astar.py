import os
import shelve
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from itertools import chain
from typing import Callable, Any, List

import numpy as np

from pampy import match
from returns.result import safe, Result
from tabulate import tabulate
from toolz import memoize
from torch import Tensor
from tqdm import tqdm

from omni_converter.solver.heap_wrapper import HeapQueue
from omni_converter.solver.rules import RuleEdge
from omni_converter.util import DefaultShelveCache
from filelock import FileLock

import cloudpickle as pickle


class NoRouteError(RuntimeError):
    pass


class ConversionError(Exception):
    pass


@dataclass
class Edge:
    src: Any
    dst: Any
    f: Callable
    cost: int
    name: str = field(default="unnamed")


def _default_inspector(x):
    return match(x,
                 Tensor, lambda t: f"Tensor:{t.shape},{t.dtype},{t.min()},{t.max()},{t.mean()}",
                 np.ndarray, lambda t: f"Numpy:{t.shape},{t.dtype},{t.min()},{t.max()},{t.mean()}",
                 list, lambda lst: f"[{_default_inspector(lst[0])}]",
                 Any, lambda t: type(t)
                 )


@dataclass
class Converter:
    edges: List[Edge]

    def _call_with_trace(self, x):
        from loguru import logger
        logger.warning(f"inspecting\n{self}")
        for e in self.edges:
            try:
                logger.warning(f"conversion:{e.src}=>{e.dst}")
                logger.warning(f"x:{_default_inspector(x)}")
                y = e.f(x)
                logger.warning(f"y:{_default_inspector(y)}")
                x = y
            except Exception:
                logger.error(f"failed to do {e.f}. due to {e}")
                return

    def __call__(self, x):
        from loguru import logger
        src = x
        init_x = x
        for e in self.edges:
            try:
                x = e.f(x)
            except Exception as ex:
                import inspect
                # TODO make this feature togglable
                logger.error(f"caught an exception. inspecting..{ex}")
                logger.warning("saving erroneous conversion for debugging")
                info = dict(
                    start=self.edges[0].src,
                    end=self.edges[-1].dst,
                    x=init_x
                )

                logger.debug(f"conversion info = start:{info['start']},x:{info['x']}")
                p = os.path.abspath("last_erroneous_conversion.pkl")
                try:
                    with open(p, "wb") as f:
                        pickle.dump(info, f)
                except Exception as save_error:
                    logger.info("failed to dump erroneous conversion.")
                    raise save_error
                    # embed()
                source: Result = safe(inspect.getsource)(e.f)
                logger.warning(f"saved last conversion error cause at {p}")
                self._call_with_trace(src)

                raise ConversionError(
                    f"exception in edge:{e.name} \n "
                    f"paths:{[e.name for e in self.edges]} \n "
                    f"x:{x} \n "
                    f"edge source:{source.value_or('failed_to_fech_source')}") from ex
        return x

    def __getitem__(self, item):
        if isinstance(item, int):
            edges = [(self.edges[item])]
        else:
            edges = self.edges[item]
        return Converter(edges)

    def __repr__(self):
        # TODO make this extendable
        replace_pairs = [
            (" ", ""),
            ("<frozendict", "<fd"),
            ("'", ""),
            ("type:", "t:"),
            ("dtype", "dt"),
            ("arrange", "ar"),
            ("ch_rpr", "ch"),
            ("v_range", "vr"),
            ("ImageDef", "ImDf")
        ]

        def replaces(tgt):
            tgt = repr(tgt)
            for a, b in replace_pairs:
                tgt = tgt.replace(a, b)
            return tgt

        path_data = [(i, e.name, (replaces(e.src)), (replaces(e.dst))) for i, e in enumerate(self.edges)]
        """
        info = OrderedDict(
            name="Conversion",
            start = start,
            end = end,
            path = path_data,
            cost = sum([e.cost for e in self.edges])
        )
        """
        # print(tabulate(path_data))
        # return pformat(info)
        if not self.edges:
            return "Converter(Identity)"
        res = f"""Converter({self.edges[0].src} => {self.edges[-1].dst}):cost={sum([e.cost for e in self.edges])}\n"""
        return res + tabulate(path_data, headers=["index", "converter", "src_format", "dst_format"])

    def trace(self, tgt):
        x = tgt
        for e in self.edges:
            x = e.f(x)
            yield dict(edge=e, x=x)


class ISolver:
    def solve(self, start_format, end_format, silent=False) -> Converter:
        pass


@dataclass
class AstarSolver(ISolver):
    heuristics: Callable
    neighbors: Callable[[Any], List[RuleEdge]]
    max_depth: int

    def __post_init__(self):
        @memoize(key=lambda args, kwargs: args)
        def memoized_solve(start, end, silent=False):
            res = self._solve(start, end, silent)
            # logger.debug("\n" + repr(res))
            return res

        self.memoized_solve = memoized_solve
        # logger.info(f"created a solver")
        # logger.debug(f"solver created with\n{self.neighbors}")

    def solve(self, start, end, silent=False) -> Converter:
        return self.memoized_solve(start, end, silent=silent)

    def _solve(self, start, end, silent) -> Converter:
        to_visit = HeapQueue()
        scores = dict()
        scores[start] = self.heuristics(start, end)
        to_visit.push(scores[start], (start, []))
        visited = 0
        if not silent:
            bar = tqdm(desc=f"solving from {start} to {end}")
        last_bar_update = visited
        search_start = datetime.now()
        timeout = timedelta(seconds=20)
        while to_visit:
            if datetime.now() - search_start >= timeout:
                raise RuntimeError(f"AstarSolver search timed out after {timeout} seconds")
            if visited - last_bar_update > 1000 and not silent:
                bar.update(visited - last_bar_update)
                last_bar_update = visited

            (pos, trace) = to_visit.pop()
            visited += 1
            if len(trace) >= self.max_depth:  # terminate search on max_depth
                continue
            if pos == end:  # reached a goal
                if not silent:
                    bar.close()
                return Converter(trace)
            if visited % 10000 == 0 and not silent:
                msg = str(pos)[:50]
                bar.set_description(f"""pos:{msg:<50}""")
            normal_nodes = self.neighbors(pos)
            # why did I choose not to provide neighbors?
            for i, ase in enumerate(normal_nodes):
                assert isinstance(ase.cost, int), f"cost is not an integer:{pos}"
                new_trace = trace + [Edge(pos, ase.new_format, ase.converter, ase.cost, ase.name)]
                try:
                    new_score = scores[pos] + ase.cost + self.heuristics(ase.new_format, end)
                except Exception as e:
                    from loguru import logger
                    logger.error(f"pos:{pos},cost:{ase.cost},next_node:{ase.new_format}")
                    raise e
                if ase.new_format in scores and scores[ase.new_format] <= new_score:
                    continue
                else:
                    scores[ase.new_format] = new_score
                    to_visit.push(new_score, (ase.new_format, new_trace))

        raise NoRouteError(f"no route found from {start} matching {end}. searched {visited} nodes.")


@dataclass
class EdgeCachedSolver_Old(ISolver):
    solver: ISolver
    cache_path: str

    def __post_init__(self):
        self.solve_cache = DefaultShelveCache(
            self._get_edges, self.cache_path
        )

        # from loguru import logger
        # logger.debug(f"using solver cache at {self.solve_cache.path}")
        @memoize
        def memoized_solve(start, end):
            key = (start, end)
            edges = self.solve_cache[key]
            assert edges is not None
            # this is taking time.
            edges = [self.solver.solve(start, end, silent=True).edges for start, end in edges]
            return Converter(list(chain(*edges)))

        self.memoized_solve = memoized_solve

    def _get_edges(self, key):
        conv = self.solver.solve(*key)
        # logger.debug(f'found conversion:\n{conv}')
        return [(e.src, e.dst) for e in conv.edges]

    def solve(self, start, end, silent=False) -> Converter:

        try:
            return self.memoized_solve(start, end)
        except Exception as e:
            from loguru import logger
            logger.error(
                f"failed to solve conversion from {start} to {end}. saving the two format as last_failed_solve.pkl due to {e}")
            with open("./last_failed_solve.pkl", "wb") as f:
                pickle.dump(dict(
                    start=start,
                    end=end
                ), f)
            raise e


@dataclass
class EdgeCachedSolver(ISolver):
    solver: ISolver
    cache_path: str

    def __post_init__(self):
        self.lock = FileLock(self.cache_path + ".lock")

        @memoize
        def memoized_solve(start, end):
            edges = self._solve_cached(start, end)
            assert edges is not None
            # this is taking time.
            edges = [self.solver.solve(start, end, silent=True).edges for start, end in edges]
            return Converter(list(chain(*edges)))

        self.memoized_solve = memoized_solve

    def open_db(self):
        return shelve.open(self.cache_path)

    def _encode_key(self, k):
        import cloudpickle as pkl
        if isinstance(k, type):
            return self._encode_key((k.__module__, k.__name__))
        elif isinstance(k, tuple):
            return ",".join([self._encode_key(e) for e in k])
        return str(pkl.dumps(k))

    def _solve_cached(self, start, end):
        import cloudpickle as pkl
        with self.open_db() as db:
            key = self._encode_key((start, end))

            if key in db:
                value = db[key]
                try:
                    return pkl.loads(value)
                except Exception:
                    from loguru import logger
                    logger.warning(f"failed to load cache for {start}=>{end}")
            res = self.solver.solve(start, end)
            edges = [(e.src, e.dst) for e in res.edges]
            value = pkl.dumps(edges)
            db[key] = value
            return edges

    def solve(self, start, end, silent=False) -> Converter:

        try:
            return self.memoized_solve(start, end)
        except Exception as e:
            from loguru import logger
            logger.error(
                f"failed to solve conversion from {start} to {end}. saving the two format as last_failed_solve.pkl due to {e}")
            with open("./last_failed_solve.pkl", "wb") as f:
                pickle.dump(dict(
                    start=start,
                    end=end
                ), f)
            raise e
