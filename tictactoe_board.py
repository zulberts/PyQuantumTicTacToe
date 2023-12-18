import numpy as np


class TicTacToeBoard:
    def __init__(self) -> None:
        self.board = np.full((3, 3, 9), " ", dtype="object")
