import numpy as np
from print_functions import transform_matrix_to_print, print_matrix


def test_regular_input():
    array = np.full((3, 3, 9), "x1")
    transformed_array = transform_matrix_to_print(array)
    assert transformed_array.shape == (9, 9)


def test_empty_array():
    array = np.zeros((3, 3, 9))
    transformed_array = transform_matrix_to_print(array)
    assert np.all(transformed_array == 0)
    assert transformed_array.shape == (9, 9)


def test_other_values():
    array = np.full((3, 3, 9), "a1")
    transformed_array = transform_matrix_to_print(array)
    assert transformed_array.shape == (9, 9)


def test_typical_matrix():
    array = np.full((3, 3, 9), " ", dtype=object)
    array[0, 0, 0] = "x1"
    array[2, 2, 8] = "x1"
    print(print_matrix(array))


test_typical_matrix()


def test_empty_matrix():
    array = np.full((3, 3, 9), " ", dtype=object)
    print(print_matrix(array))


test_empty_matrix()


def test_full_x1_matrix():
    array = np.full((3, 3, 9), "x1", dtype=object)
    print(print_matrix(array))


test_full_x1_matrix()


def test_full_X_matrix():
    array = np.full((3, 3, 9), "X", dtype=object)
    print(print_matrix(array))


test_full_X_matrix()
