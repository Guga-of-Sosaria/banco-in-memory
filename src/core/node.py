from __future__ import annotations
from typing import Any

RED = "RED"
BLACK = "BLACK"

class Node:
    #Nó da Red-Black Tree.
    __slots__ = ("key", "value", "color", "left", "right", "parent")

    def __init__(
        self,
        key: int,
        value: Any = None,
        color: str = RED,
        left: "Node | None" = None,
        right: "Node | None" = None,
        parent: "Node | None" = None,
    ) -> None:
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def is_red(self) -> bool:
        return self.color == RED

    def is_black(self) -> bool:
        return self.color == BLACK

    def __repr__(self) -> str:
        return f"Node(key={self.key!r}, color={self.color}, value={self.value!r})"


def make_nil() -> Node:
    #Cria o nó sentinela NIL.

    nil = Node(key=None, value=None, color=BLACK)  # type: ignore[arg-type]
    # Os ponteiros para si mesmo são definidos em red_black_tree.py após a criação,
    # pois o objeto ainda não existe durante __init__.
    return nil
