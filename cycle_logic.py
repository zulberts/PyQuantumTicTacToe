import numpy as np
import random


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


# creates dictionary thanks to which can be used to check who won
# creates dictionary thanks to which i can descride which pairs are
# entagled
def pairs(array: np) -> dict:
    entaglements = {'x1': [], 'o2': [], 'x3': [], 'o4': [], 'x5': [],
                    'o6': [], 'x7': [], 'o8': [], 'x9': [], 'X': [], 'O': []}
    with np.nditer(array, flags=['multi_index']) as cells:
        for cell in cells:
            if cell.item() in entaglements:
                entaglements[cell.item()].append(cells.multi_index)
    return entaglements


def pairs_entaglement(array: np) -> dict:
    entaglements = pairs(array)
    for key in list(entaglements.keys()):
        if len(entaglements[key]) < 2:
            del entaglements[key]
    entaglements.pop('X', None)
    entaglements.pop('O', None)
    return entaglements


def pairs_win(array: np) -> dict:
    entaglements = pairs(array)
    for key in list(entaglements.keys()):
        if len(entaglements[key]) < 3:
            del entaglements[key]
    return entaglements


# Chceck's if cycle occures
def cycle(adjacency_matrix, start) -> bool:
    visited = [False] * len(adjacency_matrix)
    # Creates list of vertices visited
    return dfs(adjacency_matrix, start, start, visited, None)


# Creates array(macierz sąsiedztwa) in which cells entaglement occures
def entaglement(array: np) -> np:
    adjacency_matrix_keys = {
        (0, 0): 0, (0, 1): 1, (0, 2): 2,
        (1, 0): 3, (1, 1): 4, (1, 2): 5,
        (2, 0): 6, (2, 1): 7, (2, 2): 8
    }
    adjacency_matrix = np.full((9, 9), 0, dtype=int)
    dict_entaglements = pairs_entaglement(array)
    for key in dict_entaglements.keys():
        for cell_1, cell_2 in dict_entaglements[key]:
            x = adjacency_matrix_keys[cell_1[:2]]
            y = adjacency_matrix_keys[cell_2[:2]]
            adjacency_matrix[x, y] = 1
    return adjacency_matrix


# function to if cycle occures
def replace_character(box, prefer: bool):
    if all(char == ' ' for char in box):
        return box
    elif all('x' in char or char == ' ' for char in box):
        box[4] = 'X'
    elif all('o' in char or char == ' ' for char in box):
        box[4] = 'O'
    elif any('x' in char for char in box) and any('o' in char for char in box):
        box[4] = 'X' if prefer else 'O'
    return box


# function to if cycle occures
def clear_box(box):
    return [' ' if char not in ['X', 'O'] else char for char in box]


# if cycle occures
def modify_array(array: np):
    mixed_boxes = [(i, j) for i in range(array.shape[0]) for j in range(array.shape[1])
                   if any('x' in char for char in array[i, j]) and any('o' in char for char in array[i, j])]
    random.shuffle(mixed_boxes)
    prefer = random.choice([True, False])
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if (i, j) in mixed_boxes:
                array[i, j] = replace_character(array[i, j], prefer)
                prefer = not prefer
            else:
                array[i, j] = replace_character(array[i, j])
            array[i, j] = clear_box(array[i, j])
    return array


def impossible_list(array: np):
    coordinates_correct = []
    for row in range(3):
        for col in range(3):
            if array[row][col][4] in ['X', 'O']:
                coordinates_correct.append((row, col))
    return coordinates_correct
