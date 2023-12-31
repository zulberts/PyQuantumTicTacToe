import random


def random_choose_player(array):
    available_boxes = []
    for x in range(3):
        for y in range(3):
            if array[x, y, 4] not in ['X', 'O']:
                available_boxes.append((x, y))
    if len(available_boxes) >= 2:
        return random.sample(available_boxes, 2)
    else:
        return None


def strategic_choose_player(array):
    empty_boxes = []
    for x in range(3):
        for y in range(3):
            if all(array[x, y, z] == ' ' for z in range(9)):
                empty_boxes.append((x, y))
    if len(empty_boxes) > 1:
        return random.sample(empty_boxes, 2)
    elif len(empty_boxes) == 1:
        choosen_box = empty_boxes[0]
        other_boxes = [(x, y) for x in range(3) for y in range(3)
                       if (x, y) != choosen_box]
        if other_boxes:
            return [choosen_box, random.choice(other_boxes)]
        else:
            return [choosen_box]
    else:
        return None


def get_move_value(number):
    values = ["x1", "o2", "x3", "o4", "x5", "o6", "x7", "o8", "x9"]
    if 1 <= number <= 9:
        return values[number - 1]
