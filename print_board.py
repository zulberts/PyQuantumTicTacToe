import numpy as np


class InvalidInputCoordinates(Exception):
    # Without this board could be still printed but without some
    # important data. Thanks to that exception we know that
    # some data were wrongly transfered and something wasn't
    # printed.
    def __init__(self, row, col):
        self.row = row
        self.col = col
        super().__init__(f"Invalid coordinates: row={row}, col={col}")


# This class is only responsible for printing board to terminal
class print_Board:
    """
    Class print_Board. Contains attributes:

    :param board: Contains what must be printed
    :param type: array 2-dimensional
    """

    def __init__(self) -> None:
        """
        Creates and instance of the starting board
        """
        self._board = np.full((9, 9), " ", dtype=object)

    def __str__(self) -> str:
        """
        Prints board to terminal
        """
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 39)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(f"{self._board[i, j]:^3}", end=" ")
            print()

    def __add__(self, row, col, value) -> None:
        """
        Adding to board what should be printed.
        """
        if 0 <= row < 9 and 0 <= col < 9:
            self._board[row, col] = value
        else:
            raise InvalidInputCoordinates(Exception)


if __name__ == "__main__":
    board = print_Board()

    try:
        board.__add__(3, 0, "x1")
        board.__add__(6, 0, "x1")
        board.__add__(0, 2, "x3")
        board.__add__(6, 5, "x3")
    except InvalidInputCoordinates as e:
        print(f"Caught an exception: {e}")

    board.__str__()
