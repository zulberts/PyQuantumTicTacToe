import numpy as np


def transform_matrix_to_print(array: np) -> np:
    """
    Transforms a 3D numpy array representing a quantum tic-tac-toe board into
    a 2D numpy array for easy printing.

    :param array: A 3D numpy array representing the game board.
    :type array: np
    :return: A 2D 9x9 numpy array suitable for printing the game board.
    :rtype: np
    """
    transformed_array = np.full((9, 9), " ", dtype=object)
    for i in range(3):
        for j in range(3):
            # start_row and start_col but just too long name
            row, col = 3 * i, 3 * j
            for k in range(9):
                value = array[i, j, k]
                transformed_array[row + k // 3][col + k % 3] = value
    return transformed_array


def print_matrix(array: np) -> str:
    """
    Converts the quantum tic-tac-toe game board into a formatted
    string for display.

    This function takes a 3D numpy array representing the game board and
    transforms it into a string using `transform_matrix_to_print`.
    The resulting string displays the 9x9 game board with dividers
    between each 3x3 game.

    :param array: A 3D numpy array representing the game board.
    :type array: np
    :return: A string representing the formatted game board.
    :rtype: str
    """
    array = transform_matrix_to_print(array)
    array_string = ""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            array_string += "-" * 39 + "\n"
        for j in range(9):
            if j % 3 == 0 and j != 0:
                array_string += "| "
            array_string += f"{array[i, j]:^3} "
        array_string += "\n"
    array_string.rstrip("\n")
    return array_string


def print_rules():
    """
    Print rules described in README.md.

    :return: A string representing the rules.
    :rtype: str
    """
    print(
        "Zasady gry:\n"
        "1. Gracz X zawsze zaczyna.\n"
        "2. Gracz wybiera po dwa pola w których chce postawić swój "
        "znak (x1, o2, itd.).\n"
        "   (Pola w których znajduje się X lub O są niemożliwe do wybrania.\n"
        "   Maksymalnie gra może toczyć się przez 9 rund.)\n"
        "3. Znaki (x1, o2, itd.) zamieniają się w X lub O, gdy dojdzie do "
        "cyklu.\n"
        "   (Splątanie - dwa znaki x1 lub o2 itd. tworzą splątanie. Np.: "
        "w polu nr 1 i polu nr 3\n"
        "   stoi znak x1. Wtedy te dwa pola są splątane, analogicznie z "
        "resztą znaków.\n"
        "   Cykl - zachodzi, gdy splątane pola tworzą jedno wielkie splątanie "
        "(cykl).\n"
        "   Przykład: w polach nr 1 i nr 2 stoi po znaku x1 i o2. Wtedy "
        "pole 1-2\n"
        "   jest splątane przez znak x1 oraz występuje drugie splątanie 2-1 "
        "przez znak o2.\n"
        "   Możliwe jest dojście z pola 1 do pola 2 i z powrotem do pola 1 "
        "przez drugie splątanie.\n"
        "   Ścieżki są jednokierunkowe.)\n"
        "4. Jeżeli dojdzie do splątania, wszystkie znaki na planszy "
        "zamieniają się w X lub O.\n"
        "   Jeżeli w polu występuje tylko x lub tylko o, to pole zamienia się "
        "w X lub O.\n"
        "   Jeżeli w polu znajdują się x i o, wtedy losowo w danych polach "
        "zamieniają się na X lub O.\n"
        "5. Następnie dochodzi do wygranej/remisu, jeżeli w kolumnie, rzędzie "
        "lub przekątnej\n"
        "   powstaną trzy X lub trzy O. Możliwy jest remis, gdy powstaną trzy "
        "X i trzy O w jednej konfiguracji.\n"
        "6. Gracz ma do wyboru dwóch graczy: losowego lub strategicznego "
        "(wybierającego pola bez x lub o).\n"
        "   Gracz może też wybrać, czy chce grać jako X czy jako O.\n"
        "7. Gra automatycznie sprawdza, kto wygrał i wyświetla tę wiadomość w "
        "terminalu."
    )
