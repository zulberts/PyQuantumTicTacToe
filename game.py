from players_logic import (
    random_choose_player,
    strategic_choose_player,
    get_move_value,
    input_boxes,
)
from tictactoe_board import TicTacToeBoard
from print_functions import print_rules


def main():
    print_rules()
    while True:
        print("Witaj w Kwantowym Kółko i Krzyżyk!")
        message = (
                    "Wybierz przeciwnika, jeżeli podasz złą wartość będziesz"
                    "grał przeciwko graczu \nktóry wybiera pola strategicznie"
                    " (1 - losowy, 2 - strategiczny):"
        )
        opponent = input(message)
        if opponent == "1":
            choose_player = random_choose_player
        else:
            choose_player = strategic_choose_player
        message = "Czy chcesz grać jako X czy O? Gracz X zaczyna. "
        player_symbol = input(message)
        player_starts = player_symbol.upper() == "X"
        board = TicTacToeBoard()
        round_counter = 1
        message = "Gra zakończyła się remisem ponieważ nie doszło do cyklu."
        if player_starts:
            while True:
                print(board)
                print("Twój ruch.")
                input_box1, input_box2 = input_boxes(board.impossible_moves)
                player_move_value = get_move_value(round_counter)
                board.move(player_move_value, *input_box1)
                board.move(player_move_value, *input_box2)
                board.cycle()
                win_status = board.win()
                if win_status:
                    print(win_status)
                    print(board)
                    break
                if round_counter == 9:
                    print(message)
                    break
                print("Ruch przeciwnika.")
                move_boxes = choose_player(board.board)
                computer_move_value = get_move_value(round_counter + 1)
                for box in move_boxes:
                    board.move(computer_move_value, *box)
                board.cycle()
                win_status = board.win()
                if win_status:
                    print(win_status)
                    print(board)
                    break
                round_counter += 2
        else:
            while True:
                print("Ruch przeciwnika.")
                move_boxes = choose_player(board.board)
                computer_move_value = get_move_value(round_counter)
                for box in move_boxes:
                    board.move(computer_move_value, *box)
                board.cycle()
                win_status = board.win()
                if win_status:
                    print(win_status)
                    print(board)
                    break
                print(board)
                print("Twój ruch.")
                if round_counter == 9:
                    print(message)
                    break
                input_box1, input_box2 = input_boxes(board.impossible_moves)
                player_move_value = get_move_value(round_counter + 1)
                board.move(player_move_value, *input_box1)
                board.move(player_move_value, *input_box2)
                board.cycle()
                win_status = board.win()
                if win_status:
                    print(win_status)
                    print(board)
                    break
                round_counter += 2
        play_again = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")
        if play_again.lower() != "tak":
            break


if __name__ == "__main__":
    main()
