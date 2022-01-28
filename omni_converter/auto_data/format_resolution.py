from omni_converter.solver.rules import AutoRuleBook
from pandas import DataFrame


def type_as_format(format):
    if isinstance(format, (DataFrame)):
        return [(type, "format")]


FORMAT_RESOLUTION_RULES = AutoRuleBook(
    (type_as_format,)
)
