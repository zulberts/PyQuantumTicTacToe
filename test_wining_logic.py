import numpy as np
from wining_logic import transform_matrix_to_check_win
from wining_logic import check_win


def test_matrix_with_X_and_O():
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
    output_array = np.array(
        [["X", None, None], [None, "O", None], [None, None, None]]
        )
    assert np.array_equal(transform_matrix_to_check_win(array), output_array)
    assert transform_matrix_to_check_win(array).shape == (3, 3)


def test_matrix_with_other_characters():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", "x1", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", "x1", " ", " "],
                [" ", " ", " ", "x3", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    output_array = np.array(
        [["X", None, None], [None, "O", None], [None, None, None]]
        )
    assert np.array_equal(transform_matrix_to_check_win(array), output_array)
    assert transform_matrix_to_check_win(array).shape == (3, 3)


def test_empty_matrix():
    array = np.full((3, 3, 9), " ", dtype=object)
    output_array = np.full((3, 3), None)
    assert np.array_equal(transform_matrix_to_check_win(array), output_array)
    assert transform_matrix_to_check_win(array).shape == (3, 3)


def test_matrix_full_of_X():
    array = np.full((3, 3, 9), "X", dtype=object)
    output_array = np.full((3, 3), "X")
    assert np.array_equal(transform_matrix_to_check_win(array), output_array)
    assert transform_matrix_to_check_win(array).shape == (3, 3)


def test_randomly_filled_matrix():
    values = ["X", "O", "x1", "o2", "x3", "o4", "x5", "o6", "x7", "o8", "x9"]
    array = np.random.choice(values, size=(3, 3, 9))
    array = transform_matrix_to_check_win(array)
    assert array.shape == (3, 3)


def test_win_empty_matrix():
    array = np.full((3, 3, 9), " ", dtype=object)
    assert check_win(array) is None


def test_win_matrix_full_of_x():
    array = np.full((3, 3, 9), "X", dtype=object)
    assert check_win(array) == "Gre wygrywa X!"


def test_win_matrix_full_of_o():
    array = np.full((3, 3, 9), "O", dtype=object)
    assert check_win(array) == "Gre wygrywa O!"


def test_random():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", "x1", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", "x1", " ", " "],
                [" ", " ", " ", "x3", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) is None


def test_win_random():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", "x1", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", "x1", " ", " "],
                [" ", "o4", " ", "x3", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) is None


def test_win_X_horizontal():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", "x1", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", "x1", " ", " "],
                [" ", "o4", " ", "x3", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) == "Gre wygrywa X!"


def test_win_O_horizontal():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", "x1", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", " ", " ", "O", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", " ", " ", "x1", " ", " "],
                [" ", "o4", " ", "x3", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) == "Gre wygrywa O!"


def test_win_X_vertical():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", "x1", " ", " ", "o", " ", " ", " ", " "],
                [" ", " ", " ", " ", "o", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", "X", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", "X", " ", "x1", " ", " "],
                [" ", "o4", " ", "x3", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) == "Gre wygrywa X!"


def test_win_O_vertical():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", "x1", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", "O", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", "O", " ", "x1", " ", " "],
                [" ", "o4", " ", "x3", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) == "Gre wygrywa O!"


def test_draw_vertical():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", "x1", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", "O", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", "x3", " ", " ", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", "O", " ", "x1", " ", " "],
                [" ", "o4", " ", "x3", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) == "Gra kończy się remisem!"


def test_draw_horizontal():
    array = np.array(
        [
            [
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
                [" ", "x1", " ", " ", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", "o2", " "],
            ],
            [
                [" ", " ", " ", " ", "O", " ", " ", "o2", " "],
                [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                [" ", " ", "x3", " ", "O", " ", " ", " ", " "],
            ],
            [
                [" ", " ", " ", " ", "O", " ", "x1", " ", " "],
                [" ", "o4", " ", "x3", "X", " ", " ", " ", " "],
                [" ", " ", " ", " ", "X", " ", " ", " ", " "],
            ],
        ]
    )
    assert check_win(array) == "Gra kończy się remisem!"
