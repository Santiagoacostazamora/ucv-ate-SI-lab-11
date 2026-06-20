"""
Minimax implementation.

Minimax explores every possible branch of the tree. This makes it correct,
but expensive when the tree grows.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.game_tree import GameTree


@dataclass(frozen=True)
class SearchResult:
    """Store the value found and the number of evaluated leaf nodes."""

    value: int
    nodes_evaluated: int


def is_leaf(node: GameTree) -> bool:
    """Return True when the node is a terminal score."""
    return isinstance(node, int)


def _validate_internal_node(node: GameTree) -> list[GameTree]:
    """Validate and return the children of an internal node."""
    if not isinstance(node, list):
        raise TypeError("A game tree node must be an integer leaf or a list of children.")
    if not node:
        raise ValueError("Internal tree nodes must contain at least one child.")
    return node


def minimax(node: GameTree, maximizing_player: bool = True) -> SearchResult:
    """
    Execute the Minimax algorithm over a game tree.

    Args:
        node: Tree node represented by nested lists or an integer leaf.
        maximizing_player: True when the current player maximizes.

    Returns:
        SearchResult with the best value and evaluated leaves.
    """
    if is_leaf(node):
        return SearchResult(value=node, nodes_evaluated=1)

    children = _validate_internal_node(node)
    results = [minimax(child, not maximizing_player) for child in children]
    total_nodes = sum(result.nodes_evaluated for result in results)

    if maximizing_player:
        best_value = max(result.value for result in results)
    else:
        best_value = min(result.value for result in results)

    return SearchResult(value=best_value, nodes_evaluated=total_nodes)
