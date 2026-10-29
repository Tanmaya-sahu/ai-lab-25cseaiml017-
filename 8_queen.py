
# N Queens Problem

n = int(input("Enter board size N: "))

board = [-1] * n

def safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if board[i] - i == col - row:
            return False

        if board[i] + i == col + row:
            return False

    return True

def solve(row):
    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    print("Solution:")

    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists")
