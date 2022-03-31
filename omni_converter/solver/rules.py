# rule is a class that describes a transition between states
import abc
from dataclasses import dataclass, field, replace
from typing import Callable, List, Union, NamedTuple, Tuple, Any

from lru import LRU
from pampy import match
from tabulate import tabulate

import hashlib

@dataclass()
class RuleEdge:
    converter: Callable
    new_format: object
    cost: int = field(default=1)
    name: str = field(default=None)
    is_cast: bool = field(default=False)

    def __post_init__(self):
        if self.name is None:
            self.name = self.converter.__name__


class IRule(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, state) -> List[RuleEdge]:
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass


@dataclass
class ConversionLambda(IRule):
    rule: Callable
    cost: int = field(default=1)

    def __call__(self, *args, **kwargs):
        edges = self.rule(*args, **kwargs)
        if edges is None:
            return []
        result = []

        def raise_error(e):
            raise RuntimeError(f"rule:{self.rule} returned an invalid edge:{e}")

        for edge in edges:
            e = match(edge,
                      (callable, Any),
                      lambda converter, new_state: RuleEdge(converter, new_state, self.cost, converter.__name__),
                      (callable, Any, str),
                      lambda converter, new_state, name: RuleEdge(converter, new_state, self.cost, name),
                      (callable, Any, str, int),
                      lambda converter, new_state, name, score: RuleEdge(converter, new_state, score, name),
                      (callable, Any, int, str),
                      lambda converter, new_state, score, name: RuleEdge(converter, new_state, score, name),
                      RuleEdge(callable, Any, int, str),
                      lambda converter, new_state, score, name: RuleEdge(converter, new_state, score, name),
                      RuleEdge(callable, Any, int, str, bool),
                      lambda converter, new_state, score, name, is_cast: RuleEdge(converter, new_state, score, name,
                                                                                  is_cast),
                      Any, raise_error
                      )
            result.append(e)

        return result

    def __hash__(self):
        return hash(self.rule)


def identity(x):
    return x


@dataclass
class CastLambda(IRule):
    rule: Callable
    name: str
    cost: int = field(default=1)

    def __post_init__(self):
        if self.name is None:
            cast_name = f"{self.rule.__name__}"
        else:
            cast_name = self.name
        self.cast_name = cast_name

    def __call__(self, state):
        new_states = self.rule(state)
        if new_states is not None:
            return [RuleEdge(identity, new_state, self.cost, self.cast_name, is_cast=True) for new_state in new_states]
        return None

    def __hash__(self):
        return hash((self.rule, self.name, self.cost))


class IRecursiveRule(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, format: Any, neighbor_getter: Callable[[Any], List[RuleEdge]]) -> List[RuleEdge]:
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass


class AutoRuleBook:
    def _init_non_picklable(self):
        self.memo = LRU(self.max_memo)

    def __init__(self,
                 id: str = "unknown",
                 rules: List[IRule] = None,
                 recursive_rules: List[IRecursiveRule] = None,
                 max_memo: int = 2 ** 20,
                 ):
        self.id = id
        self.max_memo = max_memo
        self._init_non_picklable()
        self.rules = tuple(rules or [])
        self.recursive_rules = tuple(recursive_rules or [])

    def __getstate__(self):
        return self.id,self.rules, self.recursive_rules, self.max_memo

    def __setstate__(self, state):
        self.id,self.rules, self.recursive_rules, self.max_memo = state
        self._init_non_picklable()

    def __add__(self, other: Union["AutoRuleBook", IRecursiveRule, IRule]):
        return match(other,
                     IRule, self.add_rule,
                     IRecursiveRule, self.add_recursive_rule,
                     AutoRuleBook,
                     lambda r: AutoRuleBook(hashlib.md5((self.id + r.id).encode()).hexdigest(), self.rules + r.rules,
                                            self.recursive_rules + r.recursive_rules),
                     )

    def add_rule(self, rule: Union[IRule, Callable]) -> "AutoRuleBook":
        """
        :param rule: any funciton that returns list of edges any of these format:
        (converter,new_state),
        (converter,new_state,name),
        (converter,new_state,score,name)
        :return:
        """
        if not isinstance(rule, IRule):
            rule = ConversionLambda(rule)
        return self + AutoRuleBook(rules=(rule,))

    def add_rules(self, *rules: Union[IRule, Callable]) -> "AutoRuleBook":
        x = self
        for r in rules:
            x = x.add_rule(r)
        return x

    def add_recursive_rule(self, r_rule: Union[IRecursiveRule, Callable]) -> "AutoRuleBook":
        if not isinstance(r_rule, (IRecursiveRule, IRule)):
            r_rule = ConversionLambda(r_rule)
        return self + AutoRuleBook(recursive_rules=[r_rule])

    def add_cast(self, rule: Callable, name=None) -> "AutoRuleBook":
        """
        :param rule: State->List[State]
        :param name:
        :return:
        """
        return self.add_rule(CastLambda(rule, name, cost=1))

    def add_alias(self, a, b) -> "AutoRuleBook":
        return self.add_cast(
            lambda state: [b] if state == a else None, name=f"alias: {a}->{b}"
        ).add_cast(
            lambda state: [a] if state == b else None, name=f"alias: {b}->{a}"
        )

    def __call__(self, state) -> List[RuleEdge]:
        return self.neighbors(state)

    def neighbors(self, state) -> List[RuleEdge]:
        if state in self.memo:
            return self.memo[state]
        else:
            for r in self.rules:
                edges = r(state)
                for e in edges or []:
                    assert isinstance(e, RuleEdge), f"r:{r}:e:{e}"
            nexts = [r(state) or [] for r in self.rules]
            recs = [rr(state, self) or [] for rr in self.recursive_rules]
            ns = nexts + recs
            res = []
            for edges in ns:
                res += edges
            if res:
                self.memo[state] = res
                return res

    def __hash__(self):
        # ohh id must return an integer, okey
        return int(hashlib.md5(self.id.encode()).hexdigest(),16)

    def __repr__(self):
        t1 = tabulate(enumerate(self.rules), headers="index rules".split())
        t2 = tabulate(enumerate(self.recursive_rules), headers="index recursive_rules".split())
        return f"AutoRuleBook(id={self.id})\n" \
               f"{t1}\n" \
               f"{t2}"

    def set_id(self, id: str):
        return AutoRuleBook(id=id, rules=self.rules, recursive_rules=self.recursive_rules, max_memo=self.max_memo)
