# Wydaje się mało optymalne używać pętli for range
# ale nie mogę znaleźć dobrego rozwiązania przy druku do terminala
# jeśli zostanie czas wrócić tutaj i postarać się poprawić to w pliku
# print_board.py
import numpy as np


def __str__(self) -> str:
    """
    Prints board to terminal
    """
    for index, x in np.ndenumerate(self._board):
        i, j = index
        if i % 3 == 0 and i != 0:
            print("-" * 39)
        if j % 3 == 0 and j != 0:
            print("|", end=" ")
        print(f"{x}", end=" ")
