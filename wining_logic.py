import numpy as np


def transform_matrix_to_check_win(input_matrix: np) -> np:
    """
    Transforms a 3D numpy array representing quantum tic-tac-toe boards into
    a 2D array to check for a win.

    :param input_matrix: A 3D numpy array representing
    quantum tic-tac-toe board.
    :type input_matrix: np
    :return: A 2D numpy array where each cell represents "X" or "O" or None.
    :rtype: np
    """
    new_matrix = np.full((3, 3), None)
    for i in range(3):
        for j in range(3):
            if "X" in input_matrix[i, j, :] or "O" in input_matrix[i, j, :]:
                new_matrix[i, j] = "X" if "X" in input_matrix[i, j, :] else "O"
    return new_matrix


def check_win(matrix: np) -> str:
    """
    Checks a quantum tic-tac-toe board to determine the game's outcome.
    This function takes a 3D numpy array representing quantum tic-tac-toe
    board and checks for a win.

    :param matrix: A 3D numpy array representing multiple tic-tac-toe boards.
    :type matrix: np.ndarray
    :return: A string declaring the winner ("X" or "O"), a draw, or None
    if the game is ongoing.
    :rtype: str
    """
    matrix = transform_matrix_to_check_win(matrix)
    win = []
    for i in range(3):
        if np.all(matrix[i, :] == "X") or np.all(matrix[:, i] == "X"):
            if "X" not in win:
                win.append("X")
        if np.all(matrix[i, :] == "O") or np.all(matrix[:, i] == "O"):
            if "O" not in win:
                win.append("O")
    normal_matrix = np.diag(matrix)
    flipped_matrix = np.diag(np.fliplr(matrix))
    if np.all(normal_matrix == "X") or np.all(flipped_matrix == "X"):
        if "X" not in win:
            win.append("X")
    if np.all(normal_matrix == "O") or np.all(flipped_matrix == "O"):
        if "O" not in win:
            win.append("O")
    if len(win) == 2:
        return "Gra kończy się remisem!"
    elif len(win) == 1:
        return f"Gre wygrywa {win[0]}!"
    elif (np.all(np.isin(matrix, ["X", "O"])) and len(win) == 0):
        return "Gra kończy się remisem!"
    else:
        return None
