from typing import List, Any



from omni_converter import __version__
from omni_converter.solver.astar import AstarSolver
from omni_converter.solver.rules import RuleEdge, AutoRuleBook


def test_version():
    assert __version__ == '0.1.0'


def _test_rule(state) -> List[RuleEdge]:
    if state == "test_state":
        return [RuleEdge(
            converter=lambda x: x + 1,
            new_state="test_state2",
            cost=1,
            name="test_state + 1"
        )]
    return []


def rule_A_to_AB(format: Any) -> List[RuleEdge]:
    if format == "A":
        # you can do any smart handling of a format here.
        return [RuleEdge(
            converter=lambda a: a + ["B"],
            new_format="AB",
            cost=1,  # optional
            name="A to AB"  # optional name to explain this conversion
        )]
    else:
        return []  # you can also return None.


def rule_AB_to_ABC(format: Any) -> List[RuleEdge]:
    if format == "AB":
        return [RuleEdge(
            converter=lambda ab: ab + ["C"],
            new_format="ABC",
            name="AB to ABC"
        )]  # omit return []


def test_example():
    solver = AstarSolver(
        heuristics=lambda x, y: 0,  # no heuristics used so it is just a BFS
        neighbors=AutoRuleBook().add_rules(
            rule_A_to_AB,
            rule_AB_to_ABC
        ),
        max_depth=100,
        silent=False  # for debugging
    )
    logger.info("\n" + repr(solver.solve("A", "ABC")))
