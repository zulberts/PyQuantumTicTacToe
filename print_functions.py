import numpy as np


def transform_matrix_print(array: np) -> np:
    transformed_array = np.full((9, 9), " ", dtype=object)
    for i in range(3):
        for j in range(3):
            # start_row and start_col but just too long name
            row, col = 3 * i, 3 * j
            for k in range(9):
                value = array[i, j, k]
                transformed_array[row + k // 3][col + k % 3] = value
    return transformed_array


def print_matrix(array: np.ndarray) -> str:
    array = transform_matrix_print(array)
    array_string = ""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            array_string += "-" * 39 + "\n"
        for j in range(9):
            if j % 3 == 0 and j != 0:
                array_string += "| "
            array_string += f"{array[i, j]:^3} "
        array_string += "\n"
    return array_string
