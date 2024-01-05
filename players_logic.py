import random
import numpy as np


def random_choose_player(array: np) -> list:
    """
    Function that imitates a player choosing two random available boxes from
    a given game board.

    :param array: The game board represented as a numpy array.
    :type array: np
    :return: A list of two randomly selected available box coordinates, or
    None if less than two boxes are available.
    :rtype: list
    """
    available_boxes = []
    for x in range(3):
        for y in range(3):
            if array[x, y, 4] not in ["X", "O"]:
                available_boxes.append((x, y))
    if len(available_boxes) >= 2:
        return random.sample(available_boxes, 2)
    else:
        return None


def strategic_choose_player(array: np) -> list:
    """
    Function that imitates a player choosing two strategic boxes based
    on the current game board status.

    :param array: The game board represented as a numpy array.
    :type array: np
    :return: A list of two strategically selected box coordinates.
    The selection is based on the emptiness and availability of the boxes.
    :rtype: list
    """
    empty_boxes = []
    for x in range(3):
        for y in range(3):
            if array[x, y, 4] not in ["X", "O"] and all(
                array[x, y, z] == " " for z in range(9)
            ):
                empty_boxes.append((x, y))
    if len(empty_boxes) > 1:
        return random.sample(empty_boxes, 2)
    elif len(empty_boxes) == 1:
        chosen_box = empty_boxes[0]
        other_boxes = []
        for x in range(3):
            for y in range(3):
                if array[x, y, 4] not in ["X", "O"] and chosen_box != (x, y):
                    other_boxes.append((x, y))
        if other_boxes:
            return [chosen_box, random.choice(other_boxes)]
        else:
            return [chosen_box]
    else:
        available_boxes = []
        for x in range(3):
            for y in range(3):
                if array[x, y, 4] not in ["X", "O"]:
                    available_boxes.append((x, y))
        if len(available_boxes) >= 2:
            return random.sample(available_boxes, 2)


def get_move_value(number: int) -> str:
    """
    Function that returns a string value corresponding to the move number in a
    quantum tic-tac-toe game.

    :param number: The move number, ranging from 1 to 9.
    :type number: int
    :return: A string representing the move value ('x1', 'o2', etc.).
    :rtype: str
    """
    values = ["x1", "o2", "x3", "o4", "x5", "o6", "x7", "o8", "x9"]
    if 1 <= number <= 9:
        return values[number - 1]


def input_boxes(impossible_moves: list) -> list:
    """
    Function to interactively take two box choices from the player,
    ensuring the choices are valid and not already taken.

    :param impossible_moves: A list of box coordinates that are not allowed
    to be chosen.
    :type impossible_moves: list
    :return: A list of two tuples, each representing the coordinates
    of the chosen boxes.
    :rtype: list
    """
    boxes = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }
    message = "Niewłaściwe wartości. Upewnij się, że podałeś liczby od 1 do 9."
    while True:
        try:
            print("Podaj dwa numery pól od 1 do 9 (oddzielone spacją):")
            values = input().split()
            if len(values) != 2:
                print("Należy podać dokładnie dwie wartości.")
                continue
            input_box1, input_box2 = map(int, values)
            box1, box2 = boxes[input_box1], boxes[input_box2]
            if box1 in impossible_moves or box2 in impossible_moves:
                print("Wybrane pola są niedozwolone. Wybierz inne.")
                continue
            return [box1, box2]
        except (ValueError, KeyError):
            print(message)
