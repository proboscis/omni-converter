def identity(x) -> Any: ...

class CastLambda:
    rule: Callable
    name: str
    cost: int

class ConversionLambda:
    rule: Callable
    cost: int

class IRecursiveRule:
    ...

class RuleEdge:
    converter: Callable
    new_format: object
    cost: int
    name: str
    is_cast: bool

class IRule:
    ...

class AutoRuleBook:
    id: str
    rules: Sequence[IRule]
    recursive_rules: Sequence[IRecursiveRule]
    max_memo: int
    def add_rule(self, rule: Union[IRule, Callable]) -> 'AutoRuleBook': ...
    def add_rules(self, *rules: Union[IRule, Callable]) -> 'AutoRuleBook': ...
    def add_recursive_rule(self, r_rule: Union[IRecursiveRule, Callable]) -> 'AutoRuleBook': ...
    def add_cast(self, rule: Callable, name = ...) -> 'AutoRuleBook': ...
    def add_alias(self, a, b) -> 'AutoRuleBook': ...
    def neighbors(self, state) -> List[RuleEdge]: ...
    def set_id(self, id: str) -> Any: ...

