import numpy as np
from players_logic import random_choose_player
from players_logic import strategic_choose_player
from players_logic import get_move_value


def test_random_empty_matrix():
    empty_matrix = np.full((3, 3, 9), " ")
    result = random_choose_player(empty_matrix)
    assert result is not None
    assert len(result) == 2
    for box in result:
        assert empty_matrix[box[0], box[1], 4] not in ["X", "O"]


def test_random_partially_filled_matrix():
    partially_filled_matrix = np.full((3, 3, 9), " ")
    partially_filled_matrix[0, 0, 4] = "X"
    partially_filled_matrix[1, 1, 4] = "O"
    partially_filled_matrix[2, 2, 4] = "X"
    result = random_choose_player(partially_filled_matrix)
    assert result is not None
    assert len(result) == 2
    for box in result:
        assert partially_filled_matrix[box[0], box[1], 4] not in ["X", "O"]


def test_random_two_boxes_matrix():
    two_boxes_matrix = np.full((3, 3, 9), "X")
    two_boxes_matrix[0, 0, 4] = " "
    two_boxes_matrix[1, 1, 4] = " "
    result = random_choose_player(two_boxes_matrix)
    assert result is not None
    assert len(result) == 2
    for box in result:
        assert two_boxes_matrix[box[0], box[1], 4] not in ["X", "O"]


def test_strategic_empty_matrix():
    empty_matrix = np.full((3, 3, 9), " ")
    result = strategic_choose_player(empty_matrix)
    assert result is not None
    assert len(result) == 2
    for box in result:
        assert empty_matrix[box[0], box[1], 4] not in ["X", "O"]


def test_strategic_partially_filled_not_XO():
    partially_filled_matrix = np.full((3, 3, 9), " ")
    partially_filled_matrix[0, 0, 0] = "A"
    partially_filled_matrix[1, 1, 8] = "B"
    result = strategic_choose_player(partially_filled_matrix)
    assert result is not None
    assert len(result) == 2
    for box in result:
        assert partially_filled_matrix[box[0], box[1], 4] not in ["X", "O"]


def test_strategic_partially_filled_XO():
    partially_filled_XO_matrix = np.full((3, 3, 9), " ")
    partially_filled_XO_matrix[0, 0, 4] = "X"
    partially_filled_XO_matrix[1, 1, 4] = "O"
    result = strategic_choose_player(partially_filled_XO_matrix)
    assert result is not None
    assert len(result) == 2
    for box in result:
        assert partially_filled_XO_matrix[box[0], box[1], 4] not in ["X", "O"]


def test_strategic_two_boxes_available():
    two_boxes_matrix = np.full((3, 3, 9), "X")
    for z in range(9):
        two_boxes_matrix[0, 0, z] = " "
        two_boxes_matrix[0, 1, z] = " "
    result = strategic_choose_player(two_boxes_matrix)
    assert result is not None
    assert len(result) == 2
    for box in result:
        assert two_boxes_matrix[box[0], box[1], 4] not in ["X", "O"]
    assert result == [(0, 0), (0, 1)]


def test_strategic_one_box_available():
    one_box_matrix = np.full((3, 3, 9), "X")
    for z in range(9):
        one_box_matrix[0, 0, z] = " "
        one_box_matrix[0, 1, z] = " "
    one_box_matrix[0, 1, 3] = "x3"
    result = strategic_choose_player(one_box_matrix)
    assert result is not None
    assert len(result) == 2
    assert result == [(0, 0), (0, 1)]


def test_get_move_value():
    for i in range(1, 10):
        expected_output = "x" if i % 2 != 0 else "o"
        expected_output += str(i)
        assert get_move_value(i) == expected_output


