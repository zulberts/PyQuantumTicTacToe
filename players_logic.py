import random
import numpy as np


def random_choose_player(array: np) -> list:
    """
    Function that imitates the player that returns random boxes.
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
    Function that imitates the player that returns strategic boxes.
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
    Function that returns what value should be placed in chosen
    by player box.
    """
    values = ["x1", "o2", "x3", "o4", "x5", "o6", "x7", "o8", "x9"]
    if 1 <= number <= 9:
        return values[number - 1]


def input_boxes(impossible_moves: list) -> list:
    """
    Function to take from player the values of whare player want
    to place his x/o.
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
