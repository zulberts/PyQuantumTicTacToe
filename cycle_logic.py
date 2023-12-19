from tictactoe_board import TicTacToeBoard
import numpy as np


# I found an algorithm named DFS that could help me to
# find if cycle occures, originally its used with graphs
# but my graph is represented by array
def dfs(adjacency_matrix, start, current, visited, parent) -> bool:
    visited[current] = True
    for neighbor in range(len(adjacency_matrix)):
        if adjacency_matrix[current][neighbor] == 1:
            if neighbor == start and parent != start:
                return True
            if not visited[neighbor]:
                if dfs(adjacency_matrix, start, neighbor, visited, current):
                    return True
    return False


# Chceck's if cycle occures
def cycle(adjacency_matrix, start) -> bool:
    visited = [False] * len(adjacency_matrix)
    # Creates list of vertices visited
    return dfs(adjacency_matrix, start, start, visited, None)


# Creates array(macierz sąsiedztwa) in which cells entaglement occures
def entaglement(array: TicTacToeBoard) -> np:
    pass
