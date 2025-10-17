from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   ", board[row][col], "   ", sep="", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")
# The function accepts one parameter containing the board's current status
# and prints it out to the console.

def enter_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit(): #ensures the input only contains digits (no letters or symbols).
            move = int(move)
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] not in ['O', 'X']:
                    board[row][col] = 'O'
                    break
                else:
                    print("Try a new spot.")
            else:
                print("Invalid move. Enter a number between 1 and 9.")
        else:
            print("Invalid input. Please enter a number.")
# The function accepts the board as a parameter,
# asks the user to enter their move (1–9),
# checks if the chosen cell is valid and unoccupied,
# and updates the board with the user's symbol ('O').


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free
# The function scans the board and builds a list of all the free squares;
# The list consists of tuples, where each tuple is a pair of row and column numbers.

def victory_for(board, sgn):
    for rc in range(3):
        if all(board[rc][c] == sgn for c in range(3)): # Check row if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return 'me' if sgn == 'X' else 'you'
        if all(board[r][rc] == sgn for r in range(3)): # Check column if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:r
            return 'me' if sgn == 'X' else 'you'
    if all(board[i][i] == sgn for i in range(3)) or all(board[i][2 - i] == sgn for i in range(3)):
        return 'me' if sgn == 'X' else 'you'
    return None
# The function checks all rows, columns, and both diagonals to determine if a player has won.
# It returns 'me' if the computer ('X') has won, 'you' if the user ('O') has won,
# or None if there is no winner yet.

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'
# The function draws the computer's move and updates the board with the computer's symbol ('X').
# It uses the make_list_of_free_fields() function to find all free squares.
# Then it randomly selects one of the free squares for its move.

# --- Main Program ---

board = [[str(3 * j + i + 1) for i in range(3)] for j in range(3)]
board[1][1] = 'X'

# Initialize the board with numbers 1–9 (as strings) so the user can identify each cell easily.
# The computer ('X') starts in the center position.
            
human_turn = True
free = make_list_of_free_fields(board)
victor = None

while free:
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("🎉 You won!")
elif victor == 'me':
    print("🤖 I won!")
else:
    print("It's a tie!")