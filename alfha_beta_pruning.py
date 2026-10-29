
# Alpha-Beta Pruning

depth = int(input("Enter depth of game tree: "))

size = 1
for i in range(depth):
    size = size * 2

values = [0] * size

for i in range(size):
    values[i] = int(input("Enter leaf value " + str(i + 1) + ": "))

def alphabeta(level, index, is_max, alpha, beta):
    if level == depth:
        return values[index]

    if is_max:
        best = float('-inf')

        for i in range(2):
            val = alphabeta(level + 1, index * 2 + i,
                            False, alpha, beta)

            if val > best:
                best = val

            if best > alpha:
                alpha = best

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(level + 1, index * 2 + i,
                            True, alpha, beta)

            if val < best:
                best = val

            if best < beta:
                beta = best

            if beta <= alpha:
                break

        return best

result = alphabeta(0, 0, True, float('-inf'), float('inf'))

print("Best Value:", result)
