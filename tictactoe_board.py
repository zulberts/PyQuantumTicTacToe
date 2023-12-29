import numpy as np
from print_functions import print_matrix
from cycle_logic import cycle, entaglement


class TicTacToeBoard:
    def __init__(self) -> None:
        """
        Creates an instance of the starting board.
        """
        self.board = np.full((3, 3, 9), " ", dtype="object")
        self.inpossible_moves = []

    # Player input, value is "x1, o2", and x, y coordinates
    # Checks if move is possible
    def move(self, value, x, y) -> bool:
        pass

    # Checks if cycle occures thanks to logic function
    # writen in other file, if occures then data in
    # array changes(cell of array becomes X or O in the center(4))
    # and new data is tranfsfered to print board
    def __cycle__(self):
        adjacency_array = entaglement(self.board)
        if cycle(adjacency_array, 0):
            # trzeba tutaj pola w ktorych powstalo X lub O
            # zamieniac na ' ' i do inpossible dodawac pola
            # do ktorych nie mozna juz dodawac ruchow
            # i w srodku pola postawic jeden X lub O zeby
            # symbolizowac ze w danym polu juz jest X lub O
            pass

    # prints board
    def __str__(self) -> None:
        print_matrix(self.board)
