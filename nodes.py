from dataclasses import dataclass
from typing import Any

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    node_a: Any
    node_b: Any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
    node_a: Any
    node_b: Any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
    node_a: Any
    node_b: Any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
    node_a: Any
    node_b: Any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"
