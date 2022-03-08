import abc
import os
from abc import ABC
from dataclasses import dataclass
from typing import Any

from cytoolz import memoize

from omni_converter.solver.rules import AutoRuleBook
from omni_converter.solver.astar import AstarSolver, Converter, EdgeCachedSolver


@memoize
def get_solver(rule: AutoRuleBook):
    solver = AstarSolver(
        heuristics=lambda x, y: 0,
        neighbors=rule,
        max_depth=100,
    )
    # ahhh we need an identifier for a rulebook.
    # the identifier needs to be consistent across runs.

    cache_path = os.path.expanduser("~/.cache/omni_converter.shelve")
    return EdgeCachedSolver(solver, cache_path)# this is too unstable
    #return solver


class IAutoData(ABC):
    @property
    @abc.abstractmethod
    def value(self):
        pass

    @property
    @abc.abstractmethod
    def format(self):
        pass

    @abc.abstractmethod
    def to(self, format):
        pass

    @abc.abstractmethod
    def convert(self, format) -> "IAutoData":
        pass

    @abc.abstractmethod
    def converter(self, format) -> Converter:
        pass

    @abc.abstractmethod
    def map(self, f, format=None) -> "IAutoData":
        pass

    @abc.abstractmethod
    def override(self, rule: AutoRuleBook) -> "IAutoData":
        pass
    @abc.abstractmethod
    def cast(self,new_format)->"IAutoData":
        pass


@dataclass
class RuledData(IAutoData):
    data: "AutoData2"
    rulebook: AutoRuleBook

    def __post_init__(self):
        self.solver = get_solver(self.rulebook)

    def __getstate__(self):
        # rulebook needs to be picklable. but it cannot be used for memo.
        # what can I do? to identify a rulebook?
        # for this I need all the rules to have ids, specified by a user.
        return self.data,self.rulebook

    def __setstate__(self,state):
        self.data,self.rulebook =state
        self.solver = get_solver(self.rulebook)

    @property
    def value(self):
        return self.data.value

    @property
    def format(self):
        return self.data.format

    def override(self, book: AutoRuleBook):
        return RuledData(self.data, book)

    def cast(self,new_format):
        return AutoData2(self.data.value,new_format).with_rules(self.rulebook)

    def converter(self, dst_format):
        conversions = self.solver.solve(self.data.format, dst_format)
        return conversions

    def convert(self, dst_format) -> "RuledData":
        convs = self.converter(dst_format)
        if convs.edges:
            return self.__class__(
                data=AutoData2(
                    value=convs(self.data.value),
                    format=convs.edges[-1].dst
                ),
                rulebook=self.rulebook
            )
        else:
            return self

    def to(self, dst_format) -> Any:
        return self.convert(dst_format).data.value

    def _repr_html_(self):
        return self.to("_repr_html_")

    def map(self, f, format=None):
        mapped = f(self.data.value)
        nv = AutoData2(
            value=mapped,
            format=format or self.format
        )
        return RuledData(
            data=nv,
            rulebook=self.rulebook,
        )


@dataclass
class AutoData2:
    value: Any
    format: Any

    def with_rules(self, rulebook: AutoRuleBook):
        return RuledData(self, rulebook)
