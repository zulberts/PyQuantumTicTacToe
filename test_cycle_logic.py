import numpy as np
from cycle_logic import (
    quantum_pairs,
    transform_list,
    pairs_entaglement,
    create_adjacency_matrix,
    cycle,
    replace_character,
    clear_box,
    modify_array,
    impossible_list
)


def test_quantum_pairs_empty_array():
    empty_array = np.full((3, 3, 9), " ")
    result_empty = quantum_pairs(empty_array)
    for key in result_empty:
        assert result_empty[key] == []


def test_quantum_pairs_mixed_matrix():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = quantum_pairs(array)
    for key in result:
        for pos in result[key]:
            assert array[pos] == key


def test_quantum_pairs_full_matrix():
    matrix = np.full((3, 3, 9), "x1")
    result = quantum_pairs(matrix)
    assert len(result["x1"]) == 3 * 3 * 9
    for key in result:
        if key != "x1":
            assert len(result[key]) == 0


def test_transform_list_empty():
    assert transform_list([]) == []


def test_transform_list_single():
    assert transform_list([(1, 2, 3)]) == [(1, 2)]


def test_transform_list_multiple():
    input_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    output_list = [(1, 2), (4, 5), (7, 8)]
    assert transform_list(input_list) == output_list


def test_quantum_pairs_entanglement_x1():
    array = np.array(
        [
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = pairs_entaglement(array)
    assert "x1" in result
    assert len(result["x1"]) == 2
    assert result["x1"] == [(0, 0), (1, 0)]
    assert "X" not in result
    assert "O" not in result


def test_pairs_entanglement_empty():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = pairs_entaglement(array)
    assert result == {}
    assert "X" not in result
    assert "O" not in result


def test_pairs_entanglement_x1_o2():
    array = np.array(
        [
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = pairs_entaglement(array)
    assert "x1" in result
    assert "o2" in result
    assert len(result["x1"]) == 2
    assert len(result["o2"]) == 2
    assert result == {"x1": [(0, 0), (1, 0)], "o2": [(0, 0), (1, 0)]}
    assert "X" not in result
    assert "O" not in result


def test_adjacency_matrix_empty():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = create_adjacency_matrix(array)
    expected = np.zeros((9, 9), dtype=int)
    assert np.array_equal(result, expected)


def test_adjacency_matrix_single_pair():
    array = np.array(
        [
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = create_adjacency_matrix(array)
    expected = np.zeros((9, 9), dtype=int)
    expected[0, 3] = 1
    expected[3, 0] = 1
    assert np.array_equal(result, expected)


def test_adjacency_matrix_two_pairs():
    array = np.array(
        [
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = create_adjacency_matrix(array)
    expected = np.zeros((9, 9), dtype=int)
    expected[0, 3] = 1
    expected[3, 0] = 1
    expected[1, 4] = 1
    expected[4, 1] = 1
    assert np.array_equal(result, expected)


def test_adjacency_matrix_three_pairs():
    array = np.array(
        [
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", "x3"],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", "x3"],
            ],
        ]
    )
    result = create_adjacency_matrix(array)
    expected = np.zeros((9, 9), dtype=int)
    expected[0, 3] = 1
    expected[3, 0] = 1
    expected[1, 4] = 1
    expected[4, 1] = 1
    expected[8, 5] = 1
    expected[5, 8] = 1
    assert np.array_equal(result, expected)


def test_adjacency_matrix_two_pairs_with_XOs():
    array = np.array(
        [
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
            ],
        ]
    )
    result = create_adjacency_matrix(array)
    expected = np.zeros((9, 9), dtype=int)
    expected[0, 3] = 1
    expected[3, 0] = 1
    expected[1, 4] = 1
    expected[4, 1] = 1
    assert np.array_equal(result, expected)


def test_adjacency_matrix_same_pairs():
    array = np.array(
        [
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    result = create_adjacency_matrix(array)
    expected = np.zeros((9, 9), dtype=int)
    expected[0, 3] = 1
    expected[3, 0] = 1
    assert np.array_equal(result, expected)


def test_cycle_occures():
    array = np.array(
        [
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    assert cycle(array, 0) is True


def test_cycle_occures_2():
    array = np.array(
        [
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", " ", "x3", " ", " ", " ", " ", " ", " "],
                [" ", "o2", "x3", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    assert cycle(array, 0) is True


def test_cycle_not_occures():
    array = np.array(
        [
            [
                ["x1", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", "o2", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    assert cycle(array, 0) is False


def test_replace_character_empty():
    box = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    output = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    assert replace_character(box, True) == output


def test_replace_character_all_x():
    box = ["x", "x", "x", "x", " ", "x", "x", "x", "x"]
    output = ["x", "x", "x", "x", "X", "x", "x", "x", "x"]
    assert replace_character(box, True) == output


def test_replace_character_all_o():
    box = ["o", "o", "o", "o", " ", "o", "o", "o", "o"]
    output = ["o", "o", "o", "o", "O", "o", "o", "o", "o"]
    assert replace_character(box, True) == output


def test_replace_character_mixed_prefer_x():
    box = ["x", "o", " ", " ", " ", " ", "o", "x", " "]
    output = ["x", "o", " ", " ", "X", " ", "o", "x", " "]
    assert replace_character(box, True) == output


def test_replace_character_mixed_prefer_o():
    box = ["x", "o", " ", " ", " ", " ", "o", "x", " "]
    assert replace_character(box, False) == [
        "x",
        "o",
        " ",
        " ",
        "O",
        " ",
        "o",
        "x",
        " ",
    ]


def test_clear_box_empty():
    box = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    assert clear_box(box) == [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def test_clear_box_with_X_O():
    box = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
    assert clear_box(box) == ["X", "O", "X", "O", "X", "O", "X", "O", "X"]


def test_clear_box_mixed():
    box = ["x2", "O", "o3", " ", "X", "x1", "O", "x4", "o5"]
    assert clear_box(box) == [" ", "O", " ", " ", "X", " ", "O", " ", " "]


def test_modify_array_with_mixed_content():
    array = np.array(
        [
            [
                ["x1", " ", " ", " ", " ", " ", " ", " ", "o2"],
                ["o2", " ", " ", " ", " ", " ", " ", " ", "x1"],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ]
            for _ in range(3)
        ],
        dtype=object,
    )
    result = modify_array(array)
    for i in range(3):
        for j in range(3):
            assert all(char in ["X", "O", " "] for char in result[i, j])


def test_modify_array_with_all_empty():
    array = np.full((3, 3, 9), " ", dtype=object)
    result = modify_array(array)
    for i in range(3):
        for j in range(3):
            assert all(char == " " for char in result[i, j])


def test_modify_array_with_all_x():
    array = np.full((3, 3, 9), "x1", dtype=object)
    result = modify_array(array)
    for i in range(3):
        for j in range(3):
            assert all(char in ["X", " "] for char in result[i, j])


def test_impossible_list_with_XOs():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
            ],
        ],
        dtype=object,
    )
    result = impossible_list(array)
    output = [(0, 0), (0, 1), (1, 1), (2, 2)]
    assert sorted(result) == sorted(output)


def test_impossible_list_without_XOs():
    array = np.full((3, 3, 9), " ", dtype=object)
    result = impossible_list(array)
    assert result == []
