import numpy as np
import random


def quantum_pairs(array: np) -> dict:
    """
    Searches through a 3D numpy array representing a quantum tic-tac-toe board
    and returns quantum pairs of 'X's and 'O's.

    :param array: A 3D numpy array representing the quantum tic-tac-toe board.
    :type array: np
    :return: A dictionary mapping each quantum pair ('x1', 'o2', etc.)
    to a list of coordinates where they occur.
    :rtype: dict
    """
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
    }
    for x in range(3):
        for y in range(3):
            for z in range(9):
                cell = array[x, y, z]
                if cell in entanglements:
                    entanglements[cell].append((x, y, z))
    return entanglements


def transform_list(list_coordinates: tuple) -> tuple:
    """
    Transforms a list of 3-dimensional coordinates to
    2-dimensional coordinates.

    :param list_coordinates: A tuple of 3-dimensional coordinates.
    :type list_coordinates: tuple
    :return: A tuple of 2-dimensional coordinates.
    :rtype: tuple
    """
    return [(x, y) for x, y, z, in list_coordinates]


def pairs_entaglement(array: np) -> dict:
    """
    Identifies and returns pairs of 2-dimensional coordinates
    that are entangled in a quantum tic-tac-toe game.

    :param array: A 3D numpy array representing the
    quantum tic-tac-toe board.
    :type array: np
    :return: A dictionary with pairs of entangled coordinates.
    :rtype: dict
    """
    entaglements = quantum_pairs(array)
    for key in list(entaglements.keys()):
        entaglements[key] = transform_list(entaglements[key])
        if len(entaglements[key]) < 2:
            del entaglements[key]
    return entaglements


def create_adjacency_matrix(array: np) -> np:
    """
    Creates an adjacency matrix from entangled pairs in a
    quantum tic-tac-toe board, useful for detecting cycles.

    :param array: A 3D numpy array representing the quantum tic-tac-toe board.
    :type array: np
    :return: An adjacency matrix representing entangled pairs.
    :rtype: np
    """
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
    """
    Depth-First Search (DFS) algorithm, typically used with graphs,
    applied here to an adjacency matrix representing
    a quantum tic-tac-toe board.

    :param adjacency_matrix: The adjacency matrix representing the game board.
    :type adjacency_matrix: np.ndarray
    :param start: The starting node for DFS.
    :param current: The current node in the DFS.
    :param visited: List of visited nodes.
    :param parent: The parent node in the DFS.
    :type start: int
    :type current: int
    :type visited: list
    :type parent: int
    :return: Boolean indicating if a cycle is found.
    :rtype: bool
    """
    visited[current] = True
    for neighbor in range(len(adjacency_matrix)):
        if adjacency_matrix[current][neighbor] == 1:
            if neighbor == start and parent != start:
                return True
            if not visited[neighbor]:
                if dfs(adjacency_matrix, start, neighbor, visited, current):
                    return True
    return False


def cycle(array: np, start: int) -> bool:
    """
    Detects if a cycle has occurred in a quantum tic-tac-toe game.

    :param array: A 3D numpy array representing the quantum tic-tac-toe board.
    :type array: np
    :param start: The starting point for cycle detection.
    :type start: int
    :return: Boolean indicating if a cycle is present.
    :rtype: bool
    """
    adjacency_matrix = create_adjacency_matrix(array)
    pairs_dict = pairs_entaglement(array)
    values = list(pairs_dict.values())
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return True
    visited = [False] * len(adjacency_matrix)
    return dfs(adjacency_matrix, start, start, visited, None)


def replace_character(box: np, prefer: bool) -> np:
    """
    Changes a box (1x9 matrix) in the quantum tic-tac-toe board
    based on whether a cycle occurs.

    :param box: A 1x9 numpy array representing a box in the
    quantum tic-tac-toe board.
    :param prefer: Boolean indicating preference between 'X' and 'O'
    if a cycle occurs.
    :type box: np
    :type prefer: bool
    :return: The modified box.
    :rtype: np
    """
    if all(char == " " for char in box):
        return box
    elif all("x" in char or char == " " for char in box):
        box[4] = "X"
    elif all("o" in char or char == " " for char in box):
        box[4] = "O"
    elif any("x" in char for char in box) and any("o" in char for char in box):
        box[4] = "X" if prefer else "O"
    return box


def clear_box(box: np) -> np:
    """
    Clears a box in the quantum tic-tac-toe board after a cycle has occurred.

    :param box: A 1x9 numpy array representing a box in the
    quantum tic-tac-toe board.
    :type box: np
    :return: The cleared box.
    :rtype: np
    """
    return [" " if char not in ["X", "O"] else char for char in box]


def modify_array(array: np) -> np:
    """
    Modifies the entire quantum tic-tac-toe board after
    cycles have been detected and resolved.

    :param array: A 3D numpy array representing the quantum tic-tac
    :type array: np
    :return: Modified array.
    :rtype: np
    """
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


def impossible_list(array: np) -> list[tuple]:
    """
    Determines which boxes in the quantum tic-tac-toe
    board are unavailable for selection after cycles.

    :param array: A 3D numpy array representing the
    quantum tic-tac-toe board.
    :type array: np.ndarray
    :return: A list of tuples representing the coordinates
    of boxes that cannot be selected.
    :rtype: list[tuple]
    """
    coordinates_incorrect = []
    for row in range(3):
        for col in range(3):
            if array[row][col][4] in ["X", "O"]:
                coordinates_incorrect.append((row, col))
    return coordinates_incorrect
