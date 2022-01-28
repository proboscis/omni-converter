import abc
from abc import ABC
from dataclasses import dataclass
from typing import Any

from cytoolz import memoize

from omni_converter.solver.rules import AutoRuleBook
from omni_converter.solver.astar import AstarSolver, Converter


@memoize
def get_solver(rule: AutoRuleBook):
    return AstarSolver(
        heuristics = lambda x,y:0,
        neighbors=rule,
        max_depth=100,
        silent=False
    )


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
    def map(self, f) -> "IAutoData":
        pass

    @abc.abstractmethod
    def override(self, rule: AutoRuleBook) -> "IAutoData":
        pass


@dataclass
class RuledData(IAutoData):
    data: "AutoData2"
    rulebook: AutoRuleBook

    def __post_init__(self):
        self.solver = get_solver(self.rulebook)

    @property
    def value(self):
        return self.data.value

    @property
    def format(self):
        return self.data.format

    def override(self, book: AutoRuleBook):
        return RuledData(self.data, book)

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

    def map(self, f):
        """
        :param f:function to convert an underlying value into a tuple of new value and its format
        :return:
        """
        mapped, format = f(self.data.value)
        nv = AutoData2(
            value=mapped,
            format=format
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
