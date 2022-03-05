__version__ = '0.1.0'

from dataclasses import dataclass
from typing import Any

from omni_converter.auto_data.auto_v2 import AutoData2, RuledData, IAutoData
from omni_converter.solver.rules import AutoRuleBook

_GLOBAL_RULE: AutoRuleBook = None


def init_global_rules(
        rulebook: AutoRuleBook
):
    global _GLOBAL_RULE
    _GLOBAL_RULE = rulebook


@dataclass
class AutoDataFactory:
    rulebook: AutoRuleBook

    def __call__(self, format, value) -> IAutoData:
        return AutoData2(value=value, format=format).with_rules(self.rulebook)
