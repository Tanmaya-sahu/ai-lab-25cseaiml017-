
# Tic-Tac-Toe

board = [" "] * 9
player = "X"
moves = 0
winner = " "

while moves < 9:
    print("\n")
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

    pos = int(input("Player " + player + ", enter position (1-9): "))

    if pos < 1 or pos > 9 or board[pos-1] != " ":
        print("Invalid position. Try again.")
        continue

    board[pos-1] = player
    moves += 1

    win = False

    # Check rows
    for i in range(0, 9, 3):
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            win = True

    # Check columns
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            win = True

    # Check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        win = True

    if board[2] == player and board[4] == player and board[6] == player:
        win = True

    if win:
        print("Player", player, "wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

if not win:
    print("Match Draw!")

print("\nFinal Board:")
for i in range(0, 9, 3):
    print(board[i], "|", board[i+1], "|", board[i+2])
