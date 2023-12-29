import numpy as np


# dostajemy macierz 3x3x9 z np i transformuje
def transform_matrix(input_matrix):
    new_matrix = np.full((3, 3), None)
    for i in range(3):
        for j in range(3):
            if 'X' in input_matrix[i, j, :] or 'O' in input_matrix[i, j, :]:
                new_matrix[i, j] = 'X' if 'X' in input_matrix[i, j, :] else 'O'
    return new_matrix


# sprawdza kto wygral i zwraca albo str z X, O lub None jak nikt
def check_win(matrix):
    for i in range(3):
        if np.all(matrix[i, :] == 'X') or np.all(matrix[:, i] == 'X'):
            return 'X'
        if np.all(matrix[i, :] == 'O') or np.all(matrix[:, i] == 'O'):
            return 'O'
    normal_matrix = np.diag(matrix)
    flipped_matrix = np.diag(np.fliplr(matrix))
    if np.all(normal_matrix == 'X') or np.all(flipped_matrix == 'X'):
        return 'X'
    if np.all(normal_matrix == 'O') or np.all(flipped_matrix == 'O'):
        return 'O'
    return None
