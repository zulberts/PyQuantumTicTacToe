import numpy as np
from print_functions import print_matrix
from cycle_logic import cycle, entaglement, modify_array, impossible_list
from wining_logic import check_win


class TicTacToeBoard:
    def __init__(self) -> None:
        """
        Creates an instance of the starting board.
        """
        self.board = np.full((3, 3, 9), " ", dtype="object")
        self.inpossible_moves = []

    def move(self, value, x, y) -> bool:
        z = int(value[1]) - 1
        if (x, y) not in self.inpossible_moves:
            self.board[x, y, z] = value
        else:
            print('Move is not possible')

    def __cycle__(self):
        adjacency_array = entaglement(self.board)
        if cycle(adjacency_array, 0):
            self.board = modify_array(self.board)
            self.inpossible_moves.extend(impossible_list(self.board))

    def __str__(self) -> None:
        print_matrix(self.board)

    def __win__(self):
        check_win(self.board)
