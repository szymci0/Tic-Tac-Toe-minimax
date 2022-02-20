# Tic-Tac-Toe with minimax alghoritm


def display_board(board, is_begin):
    blank_board = """
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""
    if is_begin:
        for i in range(1,10):
            if board[i] == 'O' or board[i] == 'X':
                blank_board = blank_board.replace(str(i), board[i])
            else:
                blank_board = blank_board.replace(str(i), ' ')
        print(blank_board)
    else:
        print(blank_board)


def player_input():
    player1 = 'X'
    while True:
        if player1.upper() == 'X':
            player2 = 'O'
            print("You've chosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        elif player1.upper() == 'O':
            player2 = 'X'
            print("You've chosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        else:
            player1 = input("Please pick a marker 'X' or 'O' ")


def evaluate(board):

    rows = [1, 4, 7]
    columns = [7, 8, 9]

    for row in rows:
        if board[row] == board[row+1] and board[row+1] == board[row+2]:
            if board[row] == 'X':
                return 10
            elif board[row]== 'O':
                return -10

    for col in columns:
        if board[col] == board[col-3] and board[col-3] == board[col-6]:
            if board[col] == 'X':
                return 10
            elif board[col]== 'O':
                return -10

    if board[1] == board[5] and board[5] == board[9]:
        if board[1] == 'X':
            return 10
        elif board[1]== 'O':
            return -10

    if board[3] == board[5] and board[5] == board[7]:
        if board[1] == 'X':
            return 10
        elif board[1]== 'O':
            return -10

    return 0


def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score

    if not full_board_check(board):
        return 0

    if is_max:
        best = -1000

        for i in range (1, 10):
            if board[i] == '#':
                board[i] = 'X'

                best = max(best, minimax(board, depth + 1, not is_max))
                board[i] = '#'
        return best
    else:
        best = 1000

        for i in range(1,10):
            if board[i]=='#':
                board[i] = 'Y'
                best = min(best, minimax(board, depth + 1, not is_max))
                board[i] = '#'
        return best


def find_best_move(board):
    best_val = -1000
    best_move = -1

    for i in range (1,10):
        if board[i] == '#':
            board[i] = 'X'
            move_val = minimax(board, 0, False)
            board[i] = '#'

            if move_val > best_val:
                best_move= i
                best_val = move_val
    print("The value of the best move is: ", best_val)
    print()
    return best_move


def check_busy(board):
    free_spaces = ['#'] * 10
    for i in range(1, 10):
        if board[i] == '#':
            free_spaces[i] = board[i]
    return free_spaces


def place_marker(board, marker, position):
    board[position] = marker
    return board


def space_check(board, position):
    return board[position] == '#'


def full_board_check(board):
    return len([x for x in board if x == '#']) == 1


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False


def player_choice(board):
    choice = input("Please select an empty space between 1 and 9 : ")
    while not space_check(board, int(choice)):
        choice = input("This space isn't free. Please choose between 1 and 9 : ")
    return choice


def replay():
    play_again = input("Do you want to play again (y/n) ? ")
    if play_again.lower() == 'y':
        return True
    if play_again.lower() == 'n':
        return False


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    i = 1
    # Choose your side
    players=player_input()
    # Empty board init
    board = ['#'] * 10
    display_board(board, 0)
    while True:
        # Set the game up here
        game_on=full_board_check(board)
        while not game_on:
            # Player to choose where to put the mark
            if i % 2 != 0:
                position = player_choice(board)
            else:
                position = find_best_move(board)
            # Who's playin ?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play
            place_marker(board, marker, int(position))
            # Check the board
            display_board(board, 1)
            i += 1
            if win_check(board, marker):
                print("You won !")
                break
            game_on=full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # Choose your side
            players = player_input()
            # Empty board init
            board = ['#'] * 10

