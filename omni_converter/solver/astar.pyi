class AstarSolver:
    heuristics: Callable
    neighbors: Callable[Any, List[RuleEdge]]
    max_depth: int
    def solve(self, start, end, silent = ...) -> Converter: ...

class ISolver:
    def solve(self, start_format, end_format, silent = ...) -> Converter: ...

class NoRouteError:
    ...

class EdgeCachedSolver_Old:
    solver: ISolver
    cache_path: str
    def solve(self, start, end, silent = ...) -> Converter: ...

class Converter:
    edges: List[Edge]
    def trace(self, tgt) -> Any: ...

class Edge:
    src: Any
    dst: Any
    f: Callable
    cost: int
    name: str

class ConversionError:
    ...

class EdgeCachedSolver:
    solver: ISolver
    cache_path: str
    def open_db(self) -> Any: ...
    def solve(self, start, end, silent = ...) -> Converter: ...

