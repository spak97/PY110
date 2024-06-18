# {
#   1: 'X', # top left
#   2: ' ', # top center
#   3: ' ', # top right
#   4: ' ', # middle left
#   5: 'O', # center
#   6: ' ', # middle right
#   7: ' ', # bottom left
#   8: ' ', # bottom center
#   9: 'X',  # bottom right
# }
def display_board(board):
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: ' ' for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def player_chooses_square(board):
    empty_squares = [key for key, value in board.items() if value == ' ']

    while True:
        prompt('Choose a square (1-9):')
        square = int(input().strip())
        if square in empty_squares:
            break
        else:
            prompt("Sorry, that's not a valid choice.")

    board[int(square)] = 'X'

board = initialize_board()
display_board(board)

player_chooses_square(board)
display_board(board)

