import pytest

from src.alpha_beta import alpha_beta
from src.game_tree import medium_tree, ordered_tree_for_pruning, sample_tree, tic_tac_toe_demo_tree
from src.minimax import minimax


def test_minimax_sample_tree_returns_expected_value():
    result = minimax(sample_tree())

    assert result.value == 5
    assert result.nodes_evaluated == 4


def test_alpha_beta_sample_tree_returns_same_value_as_minimax():
    tree = sample_tree()
    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    assert alpha_beta_result.value == minimax_result.value
    assert alpha_beta_result.nodes_evaluated <= minimax_result.nodes_evaluated


def test_minimax_medium_tree_returns_expected_value():
    result = minimax(medium_tree())

    assert result.value == 6


def test_alpha_beta_medium_tree_returns_same_value_as_minimax():
    tree = medium_tree()
    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    assert alpha_beta_result.value == minimax_result.value
    assert alpha_beta_result.nodes_evaluated <= minimax_result.nodes_evaluated


def test_alpha_beta_ordered_tree_prunes_branches():
    result = alpha_beta(ordered_tree_for_pruning())

    assert result.value == 10
    assert result.branches_pruned > 0


def test_extra_tree_keeps_both_algorithms_consistent():
    tree = tic_tac_toe_demo_tree()

    assert alpha_beta(tree).value == minimax(tree).value


def test_invalid_empty_tree_raises_value_error():
    with pytest.raises(ValueError):
        minimax([])

    with pytest.raises(ValueError):
        alpha_beta([])


def test_invalid_node_type_raises_type_error():
    with pytest.raises(TypeError):
        minimax("invalid")

    with pytest.raises(TypeError):
        alpha_beta("invalid")


def test_main_compare_algorithms_prints_report(capsys):
    from src.main import compare_algorithms

    compare_algorithms("Sample Tree", sample_tree())
    output = capsys.readouterr().out

    assert "Tree: Sample Tree" in output
    assert "Minimax value: 5" in output
    assert "Alpha-Beta value: 5" in output
