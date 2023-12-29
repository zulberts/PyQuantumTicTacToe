import numpy as np


# dostajemy macierz 3x3x9 z np i transformuje na 3x3
def transform_matrix(input_matrix: np) -> np:
    new_matrix = np.full((3, 3), None)
    for i in range(3):
        for j in range(3):
            if 'X' in input_matrix[i, j, :] or 'O' in input_matrix[i, j, :]:
                new_matrix[i, j] = 'X' if 'X' in input_matrix[i, j, :] else 'O'
    return new_matrix


# sprawdza kto wygral, moze wystapic tez remis
# zwraca string kto wygral-
def check_win(matrix: np) -> str:
    matrix = transform_matrix(matrix)
    win = []
    for i in range(3):
        if np.all(matrix[i, :] == 'X') or np.all(matrix[:, i] == 'X'):
            win.append['X']
        if np.all(matrix[i, :] == 'O') or np.all(matrix[:, i] == 'O'):
            win.append['O']
    normal_matrix = np.diag(matrix)
    flipped_matrix = np.diag(np.fliplr(matrix))
    if np.all(normal_matrix == 'X') or np.all(flipped_matrix == 'X'):
        win.append['X']
    if np.all(normal_matrix == 'O') or np.all(flipped_matrix == 'O'):
        win.append['O']
    if len(win) == 2:
        return 'Gra kończy się remisem!'
    elif len(win) == 1:
        return 'Gre wygrywa {win[0]}!'
    else:
        return None
