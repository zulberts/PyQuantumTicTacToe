import numpy as np
from print_functions import print_matrix
from wining_logic import check_win
from cycle_logic import cycle, modify_array
from cycle_logic import impossible_list, create_adjacency_matrix


class TicTacToeBoard:
    def __init__(self) -> None:
        """
        Initializes an instance of the TicTacToeBoard class,
        representing a quantum tic-tac-toe game.

        This constructor creates the initial game board,
        a 3x3x9 numpy array, where each element is an empty space.
        It initializes a list of impossible moves.
        """
        self.board = np.full((3, 3, 9), " ", dtype="object")
        self.impossible_moves = []

    def move(self, value: str, x: int, y: int) -> None:
        """
        Executes a move on the game board.

        Places the specified value at the specified
        coordinates on the board, unless the move
        is in the list of impossible moves.

        :param value: The value to be placed on the board.
        :param x: The x-coordinate for the move.
        :param y: The y-coordinate for the move.
        :type value: str
        :type x: int
        :type y: int
        """
        z = int(value[1]) - 1
        if (x, y) not in self.impossible_moves:
            self.board[x, y, z] = value
        else:
            print("Ruch nie jest możliwy")

    def cycle(self) -> None:
        """
        Checks for and resolves cycles on the game board.

        If a cycle is detected, it modifies the game board
        accordingly and updates the list of impossible moves.
        """
        ones_count = np.sum(
            create_adjacency_matrix(self.board) == 1,
            axis=1
            )
        max_ones_row = np.argmax(ones_count)
        if cycle(self.board, max_ones_row):
            self.board = modify_array(self.board)
            self.impossible_moves.extend(impossible_list(self.board))

    def __str__(self) -> str:
        """
        Represents the game board as a string for display.

        :return: A string representation of the game board.
        :rtype: str
        """
        return print_matrix(self.board)

    def win(self) -> str:
        """
        Checks if a win condition is met on the game board.

        :return: A string indicating the winner or the game.
        :rtype: str
        """
        return check_win(self.board)
