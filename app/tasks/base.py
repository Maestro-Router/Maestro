from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    description: str
    resolver: Callable[[str], str] | None = field(default=None)

    def resolve(self, query: str) -> str:
        if self.resolver:
            return self.resolver(query)
        return f"[No resolver for task {self.name}]"
