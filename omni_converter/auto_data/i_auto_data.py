import abc
from abc import ABC
from typing import TYPE_CHECKING

from omni_converter.solver.astar import Converter

if TYPE_CHECKING:
    from omni_converter.solver.rules import AutoRuleBook


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
    def override(self, rule: "AutoRuleBook") -> "IAutoData":
        pass

    @abc.abstractmethod
    def cast(self,new_format)->"IAutoData":
        pass
