#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa844602b

# Compiled with Coconut version 1.6.0 [Vocational Guidance Counsellor]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
    del _coconut_sys.modules["__coconut__"]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == "__coconut__":
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == "__coconut__":
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

import heapq  # import heapq
from loguru import logger  # from loguru import logger
from pprintpp import pformat  # from pprintpp import pformat
from collections import OrderedDict  # from collections import OrderedDict
import dill  # for pickling inner lambda...  # import dill # for pickling inner lambda...
from tqdm import tqdm  # from tqdm import tqdm
from loguru import logger  # from loguru import logger
from itertools import chain  # from itertools import chain
from os.path import expanduser  # from os.path import expanduser
import shelve  # import shelve
import os  # import os
from frozendict import frozendict  # from frozendict import frozendict
from itertools import chain  # from itertools import chain
from tabulate import tabulate  # from tabulate import tabulate
from snoop import snoop  # from snoop import snoop

from omni_converter.coconut.monad import try_monad  # from omni_converter.coconut.monad import try_monad, Success, Failure
from omni_converter.coconut.monad import Success  # from omni_converter.coconut.monad import try_monad, Success, Failure
from omni_converter.coconut.monad import Failure  # from omni_converter.coconut.monad import try_monad, Success, Failure

class Edge(_coconut.collections.namedtuple("Edge", ('src', 'dst', 'f', 'cost', 'name'))):  # data Edge(src,dst,f,cost,name="unnamed"):
    __slots__ = ()  # data Edge(src,dst,f,cost,name="unnamed"):
    __ne__ = _coconut.object.__ne__  # data Edge(src,dst,f,cost,name="unnamed"):
    def __eq__(self, other):  # data Edge(src,dst,f,cost,name="unnamed"):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  # data Edge(src,dst,f,cost,name="unnamed"):
    def __hash__(self):  # data Edge(src,dst,f,cost,name="unnamed"):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  # data Edge(src,dst,f,cost,name="unnamed"):
    __match_args__ = ('src', 'dst', 'f', 'cost', 'name')  # data Edge(src,dst,f,cost,name="unnamed"):
    def __new__(_coconut_cls, src, dst, f, cost, name="unnamed"):  # data Edge(src,dst,f,cost,name="unnamed"):
        return _coconut.tuple.__new__(_coconut_cls, (src, dst, f, cost, name))  # data Edge(src,dst,f,cost,name="unnamed"):
    def __repr__(self):  #     def __repr__(self):
        return ("Edge(<{_coconut_format_0}> -> <{_coconut_format_1}> : {_coconut_format_2})".format(_coconut_format_0=(self.src), _coconut_format_1=(self.dst), _coconut_format_2=(self.name)))  #         return f"Edge(<{self.src}> -> <{self.dst}> : {self.name})"
_coconut_call_set_names(Edge)  # class NoRouteException(Exception)
class NoRouteException(Exception): pass  # class NoRouteException(Exception)
_coconut_call_set_names(NoRouteException)  # class ConversionError(Exception)
class ConversionError(Exception): pass  # class ConversionError(Exception)
_coconut_call_set_names(ConversionError)  # class Conversion:
class Conversion:  # class Conversion:
    def __init__(self, edges):  #     def __init__(self,edges):
        self.edges = edges  #         self.edges = edges

    def __call__(self, x):  #     def __call__(self,x):
        init_x = x  #         init_x = x
        for e in self.edges:  #         for e in self.edges:
            try:  #             try:
                x = e.f(x)  #                 x = e.f(x)
            except Exception as ex:  #             except Exception as ex:
                import inspect  #                 import inspect
                import pickle  #                 import pickle
                logger.error("caught an exception. inspecting..{_coconut_format_0}".format(_coconut_format_0=(ex)))  #                 logger.error(f"caught an exception. inspecting..{ex}")
                logger.warning("saving erroneous conversion for debug".format())  #                 logger.warning(f"saving erroneous conversion for debug")
                info = dict(start=self.edges[0].src, end=self.edges[-1].dst, x=init_x)  #                 info= dict(

                logger.debug("conversion info = start:{_coconut_format_0},x:{_coconut_format_1}".format(_coconut_format_0=(info['start']), _coconut_format_1=(info['x'])))  #                 logger.debug(f"conversion info = start:{info['start']},x:{info['x']}")
                p = os.path.abspath("last_erroneous_conversion.pkl")  #                 p = os.path.abspath("last_erroneous_conversion.pkl")
                try:  #                 try:
                    with open(p, "wb") as f:  #                     with open(p,"wb") as f:
                        pickle.dump(info, f)  #                         pickle.dump(info,f)
                except Exception as save_error:  #                 except Exception as save_error:
                    from IPython import embed  #                     from IPython import embed
                    logger.info("faield to dump failed conversions.".format())  #                     logger.info(f"faield to dump failed conversions.")
                    raise save_error  #                     raise save_error
#embed()
                source = inspect.getsource(e.f)  #                 source = inspect.getsource(e.f)
                logger.warning("saved last conversion error cause at {_coconut_format_0}".format(_coconut_format_0=(p)))  #                 logger.warning(f"saved last conversion error cause at {p}")
                raise ConversionError("exception in edge:{_coconut_format_0} \n paths:{_coconut_format_1} \n x:{_coconut_format_2} \n edge source:{_coconut_format_3}".format(_coconut_format_0=(e.name), _coconut_format_1=([e.name for e in self.edges]), _coconut_format_2=(x), _coconut_format_3=(source))) from ex  #                 raise ConversionError(f"exception in edge:{e.name} \n paths:{[e.name for e in self.edges]} \n x:{x} \n edge source:{source}") from ex
        return (x)  #         return x

    def __getitem__(self, item):  #     def __getitem__(self,item):
        if isinstance(item, int):  #         if isinstance(item,int):
            edges = [(self.edges[item]), ]  #             edges = [(self.edges[item])]
        else:  #         else:
            edges = self.edges[item]  #             edges = self.edges[item]
        return (Conversion(edges))  #         return Conversion(edges)

    def __repr__(self):  #     def __repr__(self):
        replace_pairs = [(" ", ""), ("<frozendict", "<fd"), ("'", ""), ("type:", "t:"), ("dtype", "dt"), ("arrange", "ar"), ("ch_rpr", "ch"), ("v_range", "vr"), ("ImageDef", "ImDf")]  #         replace_pairs =[
        def replaces(tgt):  #         def replaces(tgt):
            tgt = repr(tgt)  #             tgt = repr(tgt)
            for a, b in replace_pairs:  #             for a,b in replace_pairs:
                tgt = tgt.replace(a, b)  #                 tgt = tgt.replace(a,b)
            return (tgt)  #             return tgt
        if len(self.edges):  #         if len(self.edges):
            start = self.edges[0].src  #             start = self.edges[0].src
            end = self.edges[-1].dst  #             end = self.edges[-1].dst
        else:  #         else:
            start = "None"  #             start = "None"
            end = "None"  #             end = "None"
        path_data = [(e.name, ((replaces)(e.src)), ((replaces)(e.dst))) for e in self.edges]  #         path_data = [(e.name,(e.src |> replaces),(e.dst |> replaces)) for e in self.edges]
        """
        info = OrderedDict(
            name="Conversion",
            start = start,
            end = end,
            path = path_data,
            cost = sum([e.cost for e in self.edges])
        )
        """  #         """
#print(tabulate(path_data))
#return pformat(info)
        res = """Conversion:(cost={_coconut_format_0})\n""".format(_coconut_format_0=(sum([e.cost for e in self.edges])))  #         res = f"""Conversion:(cost={sum([e.cost for e in self.edges])})\n"""
        return (res + tabulate(path_data))  #         return res+tabulate(path_data)
    def trace(self, tgt):  #     def trace(self,tgt):
        x = tgt  #         x = tgt
        for e in self.edges:  #         for e in self.edges:
            x = e.f(x)  #             x = e.f(x)
            yield dict(edge=e, x=x)  #             yield dict(edge= e,x=x)

_coconut_call_set_names(Conversion)  # def new_conversion(edges):
def new_conversion(edges):  # def new_conversion(edges):
    return (Conversion(edges))  #     return Conversion(edges)
class _HeapContainer:  # class _HeapContainer:
    def __init__(self, score, data):  #     def __init__(self,score,data):
        self.score = score  #         self.score = score
        self.data = data  #         self.data = data
    def __lt__(self, other):  #     def __lt__(self,other):
        return (self.score < other.score)  #         return self.score < other.score

_coconut_call_set_names(_HeapContainer)  # def _astar(
def _astar(start, matcher, neighbors, max_depth=100):  # def _astar(
    """
    neighbors: node->[(mapper,next_node,cost,name)]
    """  #     """
    to_visit = []  #     to_visit = []
    scores = dict()  #     scores = dict()
    scores[start] = 0  #heuristics(start,None)  #     scores[start] = 0#heuristics(start,None)
    heapq.heappush(to_visit, _HeapContainer(scores[start], (start, [])))  #     heapq.heappush(to_visit,
    visited = 0  #     visited = 0
    bar = tqdm(desc="solving with astar")  #     bar = tqdm(desc="solving with astar")
    while to_visit:  #     while to_visit:
        bar.update(1)  #         bar.update(1)
        hc = heapq.heappop(to_visit)  #         hc = heapq.heappop(to_visit)
        score = hc.score  #         score = hc.score
        (pos, trace) = hc.data  #         (pos,trace) = hc.data
        visited += 1  #         visited += 1
#print(f"visit:{pos}")
#print(f"{((trace[-1].a,trace[-1].name) if trace else 'no trace')}")
#print(f"visit:{trace[-1] if trace else 'no trace'}")
        if len(trace) >= max_depth:  # terminate search on max_depth  #         if len(trace) >= max_depth: # terminate search on max_depth
            logger.error("search terminated due to max_depth".format())  #             logger.error(f"search terminated due to max_depth")
            continue  #             continue
        if matcher(pos):  # reached a goal  #         if matcher(pos): # reached a goal
            logger.debug("found after {_coconut_format_0} visits.".format(_coconut_format_0=(visited)))  #             logger.debug(f"found after {visited} visits.")
            logger.debug("search result:\n{_coconut_format_0}".format(_coconut_format_0=(new_conversion(trace))))  #             logger.debug(f"search result:\n{new_conversion(trace)}")
            bar.close()  #             bar.close()
            return (trace)  #             return trace
        for mapper, next_node, cost, name in neighbors(pos):  #         for mapper,next_node,cost,name in neighbors(pos):
            assert isinstance(cost, int), "cost is not a number. cost:{_coconut_format_0},name:{_coconut_format_1},pos:{_coconut_format_2}".format(_coconut_format_0=(cost), _coconut_format_1=(name), _coconut_format_2=(pos))  #             assert isinstance(cost,int),f"cost is not a number. cost:{cost},name:{name},pos:{pos}"
            new_trace = trace + [Edge(pos, next_node, mapper, cost, name), ]  #             new_trace = trace + [Edge(pos,next_node,mapper,cost,name)]
            try:  #             try:
                new_score = scores[pos] + cost  #+ heuristics(next_node,end)  #                 new_score = scores[pos] + cost #+ heuristics(next_node,end)
            except Exception as e:  #             except Exception as e:
                logger.error("pos:{_coconut_format_0},cost:{_coconut_format_1},next_node:{_coconut_format_2}".format(_coconut_format_0=(pos), _coconut_format_1=(cost), _coconut_format_2=(next_node)))  #                 logger.error(f"pos:{pos},cost:{cost},next_node:{next_node}")
                raise e  #                 raise e
            if next_node in scores and scores[next_node] <= new_score:  #             if next_node in scores and scores[next_node] <= new_score:
                continue  #                 continue

            else:  #             else:
                scores[next_node] = new_score  #                 scores[next_node] = new_score
                heapq.heappush(to_visit, _HeapContainer(new_score, (next_node, new_trace)))  #                 heapq.heappush(to_visit,_HeapContainer(new_score,(next_node,new_trace)))

    raise NoRouteException("no route found from {_coconut_format_0} matching {_coconut_format_1}".format(_coconut_format_0=(start), _coconut_format_1=(matcher)))  #     raise NoRouteException(f"no route found from {start} matching {matcher}")



def _astar_direct(start, end, neighbors, smart_neighbors, heuristics, edge_cutter, max_depth=100, silent=False, debug_hook=None):  # def _astar_direct(
    """
    neighbors: node->[(mapper,next_node,cost,name)]
    """  #     """
    to_visit = []  #     to_visit = []
    scores = dict()  #     scores = dict()
    scores[start] = heuristics(start, end)  #     scores[start] = heuristics(start,end)
    heapq.heappush(to_visit, _HeapContainer(scores[start], (start, [])))  #     heapq.heappush(to_visit,
    visited = 0  #     visited = 0
    if not silent:  #     if not silent:
        bar = tqdm(desc="solving with astar_direct from {_coconut_format_0} to {_coconut_format_1}".format(_coconut_format_0=(start), _coconut_format_1=(end)))  #         bar = tqdm(desc=f"solving with astar_direct from {start} to {end}")
#logger.debug(f"starting search")
    last_bar_update = visited  #     last_bar_update = visited
    while to_visit:  #     while to_visit:
        if visited - last_bar_update > 1000 and not silent:  #         if visited - last_bar_update > 1000 and not silent:
            bar.update(visited - last_bar_update)  #             bar.update(visited-last_bar_update)
            last_bar_update = visited  #             last_bar_update = visited
#logger.info(f"trying to heappop from {to_visit}")
        hc = heapq.heappop(to_visit)  #         hc = heapq.heappop(to_visit)
#logger.info(f"popped container:{hc}")
        score = hc.score  #         score = hc.score
#logger.info(f"got score:{score}")
        (pos, trace) = hc.data  #         (pos,trace) = hc.data
#logger.info(f"pos:{pos},trace:{trace}")
#logger.info(f"{score}:{pos}")
        if not silent:  #         if not silent:
#bar.write(f"score:{score}")
            pass  #             pass

#logger.debug(f"visiting:{pos}")
        visited += 1  #         visited += 1
        if len(trace) >= max_depth:  # terminate search on max_depth  #         if len(trace) >= max_depth: # terminate search on max_depth
#logger.info(f"terminate search on max depth")
            continue  #             continue
        if pos == end:  # reached a goal  #         if pos == end: # reached a goal
#logger.info(f"reached goal")
            if not silent:  #             if not silent:
                logger.debug("found after {_coconut_format_0} visits.".format(_coconut_format_0=(visited)))  #                 logger.debug(f"found after {visited} visits.")
                logger.debug("search result:\n{_coconut_format_0}".format(_coconut_format_0=(new_conversion(trace))))  #                 logger.debug(f"search result:\n{new_conversion(trace)}")
                bar.close()  #                 bar.close()
#logger.info(f"returning trace")
            return (trace)  #             return trace
#logger.info(f"getting neighbors from {neighbors}")
        normal_nodes = list(neighbors(pos))  #         normal_nodes = list(neighbors(pos))
#logger.info(f"getting smart neighbors")
        smart_nodes = list(smart_neighbors(pos, end))  #         smart_nodes = list(smart_neighbors(pos,end))
#logger.debug(f"{normal_nodes},{smart_nodes}")
        if visited % 10000 == 0 and not silent:  #         if visited % 10000 == 0 and not silent:
            msg = str(pos)[:50]  #             msg = str(pos)[:50]
            bar.set_description("""pos:{_coconut_format_0:<50}""".format(_coconut_format_0=(msg)))  #             bar.set_description(f"""pos:{msg:<50}""")
        for i, (mapper, next_node, cost, name) in enumerate(chain(normal_nodes, smart_nodes)):  #         for i,(mapper,next_node,cost,name) in enumerate(chain(normal_nodes,smart_nodes)):
            assert isinstance(cost, int), "cost is not a number:{_coconut_format_0}".format(_coconut_format_0=(pos))  #             assert isinstance(cost,int),f"cost is not a number:{pos}"
            new_trace = trace + [Edge(pos, next_node, mapper, cost, name), ]  #             new_trace = trace + [Edge(pos,next_node,mapper,cost,name)]
            if debug_hook is not None:  #             if debug_hook is not None:
                debug_hook(Conversion(new_trace))  #                 debug_hook(Conversion(new_trace))
            try:  #             try:
                new_score = scores[pos] + cost + heuristics(next_node, end)  #                 new_score = scores[pos] + cost + heuristics(next_node,end)
            except Exception as e:  #             except Exception as e:
                logger.error("pos:{_coconut_format_0},cost:{_coconut_format_1},next_node:{_coconut_format_2}".format(_coconut_format_0=(pos), _coconut_format_1=(cost), _coconut_format_2=(next_node)))  #                 logger.error(f"pos:{pos},cost:{cost},next_node:{next_node}")
                raise e  #                 raise e
            if next_node in scores and scores[next_node] <= new_score:  #             if next_node in scores and scores[next_node] <= new_score:
                continue  #                 continue
            elif (edge_cutter(pos, next_node, end)):  #             elif(edge_cutter(pos,next_node,end)):
                continue  #                 continue
            else:  #             else:
                scores[next_node] = new_score  #                 scores[next_node] = new_score
                heapq.heappush(to_visit, _HeapContainer(new_score, (next_node, new_trace)))  #                 heapq.heappush(to_visit,_HeapContainer(new_score,(next_node,new_trace)))

    raise NoRouteException("no route found from {_coconut_format_0} matching {_coconut_format_1}. searched {_coconut_format_2} nodes.".format(_coconut_format_0=(start), _coconut_format_1=(end), _coconut_format_2=(visited)))  #     raise NoRouteException(f"no route found from {start} matching {end}. searched {visited} nodes.")

astar = (try_monad)((_coconut_base_compose(_astar, (new_conversion, 0))))  # astar = (_astar ..> new_conversion) |> try_monad
astar_direct = (try_monad)((_coconut_base_compose(_astar_direct, (new_conversion, 0))))  # astar_direct = (_astar_direct ..> new_conversion) |> try_monad

def _zero_heuristics(x, y):  # def _zero_heuristics(x,y):
    return (0)  #     return 0

def _no_cutter(x, y, end):  # def _no_cutter(x,y,end):
    return (False)  #     return False

MAX_MEMO = 2**(20)  # MAX_MEMO = 2**(20)

class AStarSolver:  # class AStarSolver:
    """
    to make this picklable, you have to have these caches on global variable.
    use getstate and setstate
    actually, having to pickle this solver every time you pass auto_data is not feasible.
    so, lets have auto_data to hold solver in global variable and never pickle AStarSolver!.
    so forget about lru_cache pickling issues.
    """  #     """
    def __init__(self, rules=None, smart_rules=None, heuristics=_zero_heuristics, edge_cutter=_no_cutter, cache_path=os.path.join(expanduser("~"), ".cache/autodata.shelve"), debug_hook=None):  #     def __init__(self,
        """
        rules: List[Rule]
        Rule: (state)->List[(converter:(data)->data,new_state,cost,conversion_name)]
        """  #         """
        self.rules = rules if rules is not None else []  #         self.rules = rules if rules is not None else []
        self.smart_rules = smart_rules if smart_rules is not None else []  #         self.smart_rules = smart_rules if smart_rules is not None else []
        self.heuristics = heuristics  #         self.heuristics = heuristics
        self.edge_cutter = edge_cutter  #         self.edge_cutter = edge_cutter
        logger.debug("using autodata search cache at {_coconut_format_0}".format(_coconut_format_0=(cache_path)))  #         logger.debug(f"using autodata search cache at {cache_path}")
        self.debug_hook = debug_hook  #         self.debug_hook = debug_hook
        self.cache_path = cache_path  #         self.cache_path=cache_path
        self._init_non_picklable()  #         self._init_non_picklable()

    def _init_non_picklable(self):  #     def _init_non_picklable(self):
        from lru import LRU  #         from lru import LRU
        self.neighbors_memo = LRU(MAX_MEMO)  # you cannot pickle a lru.LRU object, thus you cannot pickle this class for multiprocessing.  #         self.neighbors_memo = LRU(MAX_MEMO) # you cannot pickle a lru.LRU object, thus you cannot pickle this class for multiprocessing.
        self.search_memo = LRU(MAX_MEMO)  #         self.search_memo = LRU(MAX_MEMO)
        self.smart_neighbors_memo = LRU(MAX_MEMO)  #         self.smart_neighbors_memo = LRU(MAX_MEMO)
        self.direct_search_cache = DefaultShelveCache(lambda key: [(e.src, e.dst) for e in self._search_direct(key)], self.cache_path)  #         self.direct_search_cache = DefaultShelveCache(lambda key:[(e.src,e.dst) for e in self._search_direct(key)],self.cache_path)
        self.direct_search_memo = LRU(MAX_MEMO)  #         self.direct_search_memo = LRU(MAX_MEMO)

    def __getstate__(self):  #     def __getstate__(self):
        return (dict(rules=self.rules, smart_rules=self.smart_rules, heuristics=self.heuristics, edge_cutter=self.edge_cutter, debug_hook=self.debug_hook, cache_path=self.cache_path))  #         return dict(
    def __setstate__(self, state):  #     def __setstate__(self,state):
        self.rules = state["rules"]  #         self.rules = state["rules"]
        self.smart_rules = state["smart_rules"]  #         self.smart_rules = state["smart_rules"]
        self.heuristics = state["heuristics"]  #         self.heuristics=state["heuristics"]
        self.edge_cutter = state["edge_cutter"]  #         self.edge_cutter=state["edge_cutter"]
        self.debug_hook = state["debug_hook"]  #         self.debug_hook=state["debug_hook"]
        self.cache_path = state["cache_path"]  #         self.cache_path=state["cache_path"]
        self._init_non_picklable()  #         self._init_non_picklable()

    def neighbors(self, node):  #     def neighbors(self,node):
#logger.info(f"trying to get neighbors")
        if node in self.neighbors_memo:  #         if node in self.neighbors_memo:
            return (self.neighbors_memo[node])  #             return self.neighbors_memo[node]

        res = []  #         res = []
        for rule in self.rules:  #         for rule in self.rules:
#logger.info(f"checking rule:{rule}")
            edges = rule(node)  #             edges = rule(node)
#logger.info(f"got rules:{edges}")
            if edges is not None:  #             if edges is not None:
                res += edges  #                  res += edges
#logger.info(f"memorizing neighbors")
        self.neighbors_memo[node] = res  #         self.neighbors_memo[node] = res
#logger.info(f"memorized neighbors")
        return (res)  #         return res
    def smart_neighbors(self, node, end):  #     def smart_neighbors(self,node,end):
        if (node, end) in self.smart_neighbors_memo:  #         if (node,end) in self.smart_neighbors_memo:
            return (self.smart_neighbors_memo[(node, end)])  #             return self.smart_neighbors_memo[(node,end)]
        res = []  #         res = []
        for rule in self.smart_rules:  #         for rule in self.smart_rules:
            edges = rule(node, end)  #             edges = rule(node,end)
            if edges is not None:  #             if edges is not None:
                res += edges  #                 res += edges
        self.smart_neighbors_memo[(node, end)] = res  #         self.smart_neighbors_memo[(node,end)] = res
#logger.debug(res)
        return (res)  #         return res

    def invalidate_cache(self):  #     def invalidate_cache(self):
        self.neighbors_memo.clear()  #         self.neighbors_memo.clear()
        self.search_memo.clear()  #         self.search_memo.clear()
        self.direct_search_memo.clear()  #         self.direct_search_memo.clear()

    def add_rule(self, f):  #     def add_rule(self,f):
        self.rules.append(f)  #         self.rules.append(f)
        self.invalidate_cache()  #         self.invalidate_cache()

    def search(self, start, matcher):  #     def search(self,start,matcher):
#problem is that you can't hash matcher
#let's use id of matcher for now.
        q = (start, id(matcher))  #         q = (start,id(matcher))
        if q in self.search_memo:  #         if q in self.search_memo:
            res = self.search_memo[q]  #             res = self.search_memo[q]
        else:  #         else:
            logger.debug("searching from {_coconut_format_0} for matching {_coconut_format_1}".format(_coconut_format_0=(start), _coconut_format_1=(matcher)))  #             logger.debug(f"searching from {start} for matching {matcher}")
            res = astar(start=start, matcher=matcher, neighbors=self.neighbors)  #             res = astar(
            self.search_memo[q] = res  #             self.search_memo[q] = res

        _coconut_case_match_to_0 = res  #         case res:
        _coconut_case_match_check_0 = False  #         case res:
        _coconut_match_set_name_res = _coconut_sentinel  #         case res:
        if (_coconut.isinstance(_coconut_case_match_to_0, Success)) and (_coconut.len(_coconut_case_match_to_0) == 1):  #         case res:
            _coconut_match_set_name_res = _coconut_case_match_to_0[0]  #         case res:
            _coconut_case_match_check_0 = True  #         case res:
        if _coconut_case_match_check_0:  #         case res:
            if _coconut_match_set_name_res is not _coconut_sentinel:  #         case res:
                res = _coconut_case_match_to_0[0]  #         case res:
        if _coconut_case_match_check_0:  #         case res:
            return (res)  #                 return res
        if not _coconut_case_match_check_0:  #             match Failure(e,trc):
            _coconut_match_set_name_e = _coconut_sentinel  #             match Failure(e,trc):
            _coconut_match_set_name_trc = _coconut_sentinel  #             match Failure(e,trc):
            if (_coconut.isinstance(_coconut_case_match_to_0, Failure)) and (_coconut.len(_coconut_case_match_to_0) == 2):  #             match Failure(e,trc):
                _coconut_match_set_name_e = _coconut_case_match_to_0[0]  #             match Failure(e,trc):
                _coconut_match_set_name_trc = _coconut_case_match_to_0[1]  #             match Failure(e,trc):
                _coconut_case_match_check_0 = True  #             match Failure(e,trc):
            if _coconut_case_match_check_0:  #             match Failure(e,trc):
                if _coconut_match_set_name_e is not _coconut_sentinel:  #             match Failure(e,trc):
                    e = _coconut_case_match_to_0[0]  #             match Failure(e,trc):
                if _coconut_match_set_name_trc is not _coconut_sentinel:  #             match Failure(e,trc):
                    trc = _coconut_case_match_to_0[1]  #             match Failure(e,trc):
            if _coconut_case_match_check_0:  #             match Failure(e,trc):
                raise e  #                 raise e
    def _research_from_edges(self, edges):  #     def _research_from_edges(self,edges):
        searched_edges = list(chain(*[self._search_direct((src, dst, True)).edges for src, dst in edges]))  #         searched_edges = list(chain(*[self._search_direct((src,dst,True)).edges for src,dst in edges]))
#logger.info(f"searched_edges:{searched_edges}")
        return (Conversion(searched_edges))  #         return Conversion(searched_edges)

    def _search_direct(self, q):  #     def _search_direct(self,q):
# you cannot directly save the function.
# so you need to save the paths and re-search it
        start, end, silent = q  #         start,end,silent = q
        if not silent:  #         if not silent:
            logger.debug("searching {_coconut_format_0} to {_coconut_format_1}".format(_coconut_format_0=(start), _coconut_format_1=(end)))  #             logger.debug(f"searching {start} to {end}")
        res = astar_direct(start=start, end=end, neighbors=self.neighbors, smart_neighbors=self.smart_neighbors, heuristics=self.heuristics, edge_cutter=self.edge_cutter, silent=silent, debug_hook=self.debug_hook)  #         res = astar_direct(
        _coconut_case_match_to_1 = res  #             start=start,
        _coconut_case_match_check_1 = False  #             start=start,
        _coconut_match_set_name_res = _coconut_sentinel  #             start=start,
        if (_coconut.isinstance(_coconut_case_match_to_1, Success)) and (_coconut.len(_coconut_case_match_to_1) == 1):  #             start=start,
            _coconut_match_set_name_res = _coconut_case_match_to_1[0]  #             start=start,
            _coconut_case_match_check_1 = True  #             start=start,
        if _coconut_case_match_check_1:  #             start=start,
            if _coconut_match_set_name_res is not _coconut_sentinel:  #             start=start,
                res = _coconut_case_match_to_1[0]  #             start=start,
        if _coconut_case_match_check_1:  #             start=start,
            return (res)  #                 return res
        if not _coconut_case_match_check_1:  #             match Failure(e,trc):
            _coconut_match_set_name_e = _coconut_sentinel  #             match Failure(e,trc):
            _coconut_match_set_name_trc = _coconut_sentinel  #             match Failure(e,trc):
            if (_coconut.isinstance(_coconut_case_match_to_1, Failure)) and (_coconut.len(_coconut_case_match_to_1) == 2):  #             match Failure(e,trc):
                _coconut_match_set_name_e = _coconut_case_match_to_1[0]  #             match Failure(e,trc):
                _coconut_match_set_name_trc = _coconut_case_match_to_1[1]  #             match Failure(e,trc):
                _coconut_case_match_check_1 = True  #             match Failure(e,trc):
            if _coconut_case_match_check_1:  #             match Failure(e,trc):
                if _coconut_match_set_name_e is not _coconut_sentinel:  #             match Failure(e,trc):
                    e = _coconut_case_match_to_1[0]  #             match Failure(e,trc):
                if _coconut_match_set_name_trc is not _coconut_sentinel:  #             match Failure(e,trc):
                    trc = _coconut_case_match_to_1[1]  #             match Failure(e,trc):
            if _coconut_case_match_check_1:  #             match Failure(e,trc):
                raise e  #                 raise e

    def search_direct(self, start, end, silent=False):  #     def search_direct(self,start,end,silent=False):
        key = (start, end, silent)  #         key = (start,end,silent)
        if key in self.direct_search_memo:  #         if key in self.direct_search_memo:
            return (self.direct_search_memo[key])  #             return self.direct_search_memo[key]
        elif key in self.direct_search_cache:  #         elif key in self.direct_search_cache:
            edges = self.direct_search_cache[key]  #             edges = self.direct_search_cache[key]
            conversion = self._research_from_edges(edges)  #             conversion = self._research_from_edges(edges)
            self.direct_search_memo[key] = conversion  #             self.direct_search_memo[key] = conversion
#logger.debug(f"researched_conversion:\n{conversion}")
            return (conversion)  #             return conversion
        else:  #         else:
            conversion = self._search_direct(key)  #             conversion = self._search_direct(key)
#logger.info(f"caching conversion:\n{conversion}")
            self.direct_search_cache[key] = [(e.src, e.dst) for e in conversion.edges]  #             self.direct_search_cache[key] = [(e.src,e.dst) for e in conversion.edges]
            self.direct_search_memo[key] = conversion  #             self.direct_search_memo[key] = conversion
# I can memo every path in conversion actually.
# however since the states are in a different space than a query, no speedups can be done.
# if this astar knows about casting, it can first search for a cache though..

            return (conversion)  #             return conversion

    def search_direct_any(self, start, ends):  #     def search_direct_any(self,start,ends):
        for cand in ends:  #         for cand in ends:
            try:  #             try:
                res = self.search_direct(start, cand)  #                 res = self.search_direct(start,cand)
                return (res)  #                 return res
            except Exception as e:  #             except Exception as e:
                pass  #                 pass
        raise NoRouteException("no route found from {_coconut_format_0} to any of {_coconut_format_1}".format(_coconut_format_0=(start), _coconut_format_1=(ends)))  #         raise NoRouteException(f"no route found from {start} to any of {ends}")


_coconut_call_set_names(AStarSolver)  #
