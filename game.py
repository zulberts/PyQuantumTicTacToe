from tictactoe_board import TicTacToeBoard
from print_functions import print_matrix

def main():
    board = TicTacToeBoard()
    current_player = 0
    players = ['X', 'O']

    while True:
        print_matrix(board.board)
        break


if __name__ == "__main__":
    main()