import random
def start_game():
    print("TicTacToe")
    print("If you want to play singleplayer input 'S'\n"
          "If you want to play multiplayer input 'M'")
    game = input("Type 'S' or 'M' :")

    return game

def print_board(board):
    for column in board:
        for cell in column:
            print(cell, end = " ")
        print()

def check_play(play, board, turn):
    if play in range(1, 4):
        column = board[0]
        if play in column:
            played_index = column.index(play)
            column[played_index] = turn
            board[0] = column
        else:
            while play not in column:
                print("Invalid move")
                play = int(input(f"{turn}'s turn :"))

            played_index = column.index(play)
            column[played_index] = turn
            board[0] = column
    elif play in range(4, 7):
        column = board[1]
        if play in column:
            played_index = column.index(play)
            column[played_index] = turn
            board[1] = column
        else:
            while play not in column:
                print("Invalid move")
                play = int(input(f"{turn}'s turn :"))

            played_index = column.index(play)
            column[played_index] = turn
            board[1] = column
    else:
        column = board[2]
        if play in column:
            played_index = column.index(play)
            column[played_index] = turn
            board[2] = column
        else:
            while play not in column:
                print("Invalid move")
                play = int(input(f"{turn}'s turn :"))

            played_index = column.index(play)
            column[played_index] = turn
            board[2] = column

def update_board(board, play):
    if play in range(1, 4):
        column = board[0]
        played_index = column.index(play)
        column[played_index] = "O"
        board[0] = column
    elif play in range(4, 7):
        column = board[1]
        played_index = column.index(play)
        column[played_index] = "O"
        board[1] = column
    else:
        column = board[2]
        played_index = column.index(play)
        column[played_index] = "O"
        board[2] = column

def get_playable_positions(board):
    playable_positions = []
    for column in board:
        for cell in column:
            if type(cell) == int:
                playable_positions.append(cell)
            else:
                pass
    return playable_positions

def check_winner(board):
    column_1 = board[0]
    column_2 = board[1]
    column_3 = board[2]
    winning_combinations = [
        [column_1[0], column_1[2], column_1[4]],
        [column_2[0], column_2[2], column_2[4]],
        [column_3[0], column_3[2], column_3[4]],
        [column_1[0], column_2[0], column_3[0]],
        [column_1[2], column_2[2], column_3[2]],
        [column_1[4], column_2[4], column_3[4]],
        [column_1[0], column_2[2], column_3[4]],
        [column_1[4], column_2[2], column_3[0]]
    ]

    for winning_combination in winning_combinations:
        if "X" == winning_combination[0] and "X" == winning_combination[1] and "X" == winning_combination[2]:
            win = True
            winner = "X"
            break
        elif "O" == winning_combination[0] and "O" == winning_combination[1] and "O" == winning_combination[2]:
            win = True
            winner = "O"
            break
        else:
            win = False
            winner = "Tie"

    return [win, winner]

def singleplayer_game():
    board = [[1, "|", 2, "|", 3], [4, "|", 5, "|", 6], [7, "|", 8, "|", 9]]
    print_board(board)
    turn = 1
    win = False

    while turn < 10 and win == False:
        if turn % 2 != 0:
            play = int(input("X's turn :"))
            while play not in range(1, 10):
                play = int(input("X's turn :"))

            check_play(play, board, "X")
            print_board(board)
            print()
        else:
            playable_positions = get_playable_positions(board)
            play = random.choice(playable_positions)
            print(f"O plays {play}")
            update_board(board, play)
            print_board(board)
            print()
        turn = turn + 1
        winner = check_winner(board)
        win = check_winner(board)[0]

    if win == True:
        print(f"{winner[1]} wins")
    else:
        print(winner[1])

def multiplayer_game():
    x_player = input("X player enter your name :")
    o_player = input("O player input your name :")
    board = [[1, "|", 2, "|", 3], [4, "|", 5, "|", 6], [7, "|", 8, "|", 9]]
    print_board(board)
    turn = 1
    win = False

    while turn < 10 and win == False:
        if turn % 2 != 0:
            play = int(input(f"{x_player}'s turn :"))
            while play not in range(1, 10):
                play = int(input(f"{x_player}'s turn :"))

            check_play(play, board, "X")
            print_board(board)
            print()
        else:
            play = int(input(f"{o_player}'s turn :"))
            while play not in range(1, 10):
                play = int(input(f"{o_player}'s turn :"))

            check_play(play, board, "O")
            print_board(board)
            print()
        turn = turn + 1
        winner = check_winner(board)
        win = check_winner(board)[0]

    if win == True:
        if winner[1] == "X":
            print(f"{x_player} wins")
        else:
            print(f"{o_player} wins")
    else:
        print(winner[1])

def play_tictactoe():
    game = start_game()

    if game == "S":
        singleplayer_game()
    elif game == "M":
        multiplayer_game()
    else:
        print("Invalid choice")

play_tictactoe()