"""
Game tree examples for the Minimax and Alpha-Beta laboratory.

A tree is represented using nested lists:
- Internal nodes are lists.
- Leaf nodes are integer scores.

The maximizing player tries to obtain the highest value.
The minimizing player tries to obtain the lowest value.
"""

from __future__ import annotations

from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]


def sample_tree() -> GameTree:
    """Return a small tree for classroom demonstration. Expected result: 5."""
    return [
        [5, 8],
        [2, 9],
    ]


def medium_tree() -> GameTree:
    """Return a medium-sized tree where Alpha-Beta can prune. Expected result: 6."""
    return [
        [[3, 6], [6, 9]],
        [[1, 2], [0, -1]],
        [[4, 4], [5, 6]],
    ]


def ordered_tree_for_pruning() -> GameTree:
    """Return a tree ordered to help Alpha-Beta prune. Expected result: 10."""
    return [
        [[10, 9], [10, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]


def tic_tac_toe_demo_tree() -> GameTree:
    """Return an additional example inspired by a simple game decision tree."""
    return [
        [[1, 0], [-1, 1]],
        [[0, -1], [1, 0]],
        [[-1, -1], [0, 1]],
    ]
