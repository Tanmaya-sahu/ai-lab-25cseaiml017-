
# Minimax Algorithm

depth = int(input("Enter depth of game tree: "))

size = 1
for i in range(depth):
    size = size * 2

values = [0] * size

for i in range(size):
    values[i] = int(input("Enter leaf value " + str(i + 1) + ": "))

def minimax(level, index, is_max):
    if level == depth:
        return values[index]

    left = minimax(level + 1, index * 2, not is_max)
    right = minimax(level + 1, index * 2 + 1, not is_max)

    if is_max:
        if left > right:
            return left
        else:
            return right
    else:
        if left < right:
            return left
        else:
            return right

result = minimax(0, 0, True)

print("Best Minimax Value:", result)
