import numpy as np
import random


def pairs(array: np) -> dict:
    entanglements = {
        "x1": [],
        "o2": [],
        "x3": [],
        "o4": [],
        "x5": [],
        "o6": [],
        "x7": [],
        "o8": [],
        "x9": [],
        "X": [],
        "O": [],
    }
    for x in range(3):
        for y in range(3):
            for z in range(9):
                cell = array[x, y, z]
                if cell in entanglements:
                    entanglements[cell].append((x, y, z))
    return entanglements


def transform_list(list_coordinates):
    return [(x, y) for x, y, z, in list_coordinates]


def pairs_entaglement(array: np) -> dict:
    entaglements = pairs(array)
    for key in list(entaglements.keys()):
        entaglements[key] = transform_list(entaglements[key])
        if len(entaglements[key]) < 2:
            del entaglements[key]
    entaglements.pop("X", None)
    entaglements.pop("O", None)
    return entaglements


def create_adjacency_matrix(array):
    adjacency_matrix_keys = {
        (0, 0): 0,
        (0, 1): 1,
        (0, 2): 2,
        (1, 0): 3,
        (1, 1): 4,
        (1, 2): 5,
        (2, 0): 6,
        (2, 1): 7,
        (2, 2): 8,
    }
    adjacency_matrix = np.zeros((9, 9), dtype=int)
    pairs_dict = pairs_entaglement(array)
    for pairs in pairs_dict.values():
        if len(pairs) == 2:
            x, y = pairs
            cell_x = adjacency_matrix_keys[x]
            cell_y = adjacency_matrix_keys[y]
            adjacency_matrix[cell_x, cell_y] = 1
            adjacency_matrix[cell_y, cell_x] = 1
    return adjacency_matrix


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


def cycle(array: np, start) -> bool:
    adjacency_matrix = create_adjacency_matrix(array)
    pairs_dict = pairs_entaglement(array)
    values = list(pairs_dict.values())
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return True
    visited = [False] * len(adjacency_matrix)
    return dfs(adjacency_matrix, start, start, visited, None)


def replace_character(box, prefer: bool):
    if all(char == " " for char in box):
        return box
    elif all("x" in char or char == " " for char in box):
        box[4] = "X"
    elif all("o" in char or char == " " for char in box):
        box[4] = "O"
    elif any("x" in char for char in box) and any("o" in char for char in box):
        box[4] = "X" if prefer else "O"
    return box


def clear_box(box):
    return [" " if char not in ["X", "O"] else char for char in box]


def modify_array(array: np):
    mixed_boxes = [
        (i, j)
        for i in range(array.shape[0])
        for j in range(array.shape[1])
        if any("x" in char for char in array[i, j])
        and any("o" in char for char in array[i, j])
    ]
    random.shuffle(mixed_boxes)
    prefer = random.choice([True, False])
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if (i, j) in mixed_boxes:
                array[i, j] = replace_character(array[i, j], prefer)
                prefer = not prefer
            else:
                array[i, j] = replace_character(array[i, j], prefer)
            array[i, j] = clear_box(array[i, j])
    return array


def impossible_list(array: np):
    coordinates_correct = []
    for row in range(3):
        for col in range(3):
            if array[row][col][4] in ["X", "O"]:
                coordinates_correct.append((row, col))
    return coordinates_correct
