import numpy as np
from print_functions import print_matrix
from wining_logic import check_win
from cycle_logic import cycle, create_adjacency_matrix, modify_array
from cycle_logic import impossible_list


class TicTacToeBoard:
    def __init__(self) -> None:
        """
        Creates an instance of the starting board.
        """
        self.board = np.full((3, 3, 9), " ", dtype="object")
        self.impossible_moves = []

    def move(self, value, x, y):
        z = int(value[1]) - 1
        if (x, y) not in self.impossible_moves:
            self.board[x, y, z] = value
        else:
            print("Move is not possible")

    def __cycle__(self):
        adjacency_array = create_adjacency_matrix(self.board)
        if cycle(adjacency_array, 0):
            self.board = modify_array(self.board)
            self.impossible_moves.extend(impossible_list(self.board))

    def __str__(self) -> str:
        return print_matrix(self.board)

    def __win__(self):
        check_win(self.board)
