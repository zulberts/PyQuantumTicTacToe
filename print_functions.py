import numpy as np


def transform_matrix_to_print(array: np) -> np:
    """
    Transforms a 3D numpy array representing a quantum tic-tac-toe board into
    a 2D numpy array for easy printing.

    :param array: A 3D numpy array representing the game board.
    :type array: np
    :return: A 2D 9x9 numpy array suitable for printing the game board.
    :rtype: np
    """
    transformed_array = np.full((9, 9), " ", dtype=object)
    for i in range(3):
        for j in range(3):
            # start_row and start_col but just too long name
            row, col = 3 * i, 3 * j
            for k in range(9):
                value = array[i, j, k]
                transformed_array[row + k // 3][col + k % 3] = value
    return transformed_array


def print_matrix(array: np) -> str:
    """
    Converts the quantum tic-tac-toe game board into a formatted
    string for display.

    This function takes a 3D numpy array representing the game board and
    transforms it into a string using `transform_matrix_to_print`.
    The resulting string displays the 9x9 game board with dividers
    between each 3x3 game.

    :param array: A 3D numpy array representing the game board.
    :type array: np
    :return: A string representing the formatted game board.
    :rtype: str
    """
    array = transform_matrix_to_print(array)
    array_string = ""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            array_string += "-" * 39 + "\n"
        for j in range(9):
            if j % 3 == 0 and j != 0:
                array_string += "| "
            array_string += f"{array[i, j]:^3} "
        array_string += "\n"
    array_string.rstrip('\n')
    return array_string
