import numpy as np


class TicTacToeBoard:
    def __init__(self) -> None:
        """
        Creates an instance of the starting board.
        """
        self.board = np.full((3, 3, 9), " ", dtype="object")

    # Player input, value is "x1, o2", and x, y coordinates
    # Checks if move is possible
    def move(self, value, x, y) -> bool:
        pass

    # Checks if cycle occures thanks to logic function
    # writen in other file, if occures then data in
    # array changes(cell of array becomes X or O in the center(4))
    # and new data is tranfsfered to print board
    def check_cycle_occures(self) -> bool:
        pass

    # Imports data to print board
    def import_to_print(self) -> None:
        pass
