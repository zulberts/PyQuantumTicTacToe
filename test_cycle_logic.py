from cycle_logic import cycle, entaglement
import numpy as np


adjacency_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
start = 0
if cycle(adjacency_matrix, start):
    print("Cycle has occured")
else:
    print("There is no cycle")


def create_empty_board():
    return np.full((3, 3, 9), ' ', dtype=str)


def test_entaglement_simple():
    board = create_empty_board()
    result = entaglement(board)
    assert np.all(result == np.zeros((9, 9)))
