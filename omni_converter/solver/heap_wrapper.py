import heapq
from dataclasses import dataclass, field
from typing import TypeVar, Any, Generic, List

T = TypeVar("T")


@dataclass
class HeapContainer:
    score: int
    data: Any

    def __lt__(self, other):
        return self.score < other.score


@dataclass
class HeapQueue(Generic[T]):
    data: List[HeapContainer] = field(default_factory=list)

    def push(self, score, data):
        heapq.heappush(self.data, HeapContainer(score, data))

    def __bool__(self):
        return len(self.data) != 0

    def pop(self) -> T:
        return heapq.heappop(self.data).data
