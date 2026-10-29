
# Water Jug Problem

a = int(input("Enter capacity of Jug 1: "))
b = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

queue = [(0, 0)]
visited = []
parent = []

front = 0
found = False
goal = (-1, -1)

visited.append((0, 0))
parent.append((-1, -1))

while front < len(queue):
    x, y = queue[front]
    front += 1

    if x == target or y == target:
        found = True
        goal = (x, y)
        break

    states = [
        (a, y),                    # Fill jug 1
        (x, b),                    # Fill jug 2
        (0, y),                    # Empty jug 1
        (x, 0),                    # Empty jug 2
        (x - (b-y if x > b-y else x),
         y + (x if x < b-y else b-y)),  # Pour 1 to 2
        (x + (y if y < a-x else a-x),
         y - (y if y < a-x else a-x))   # Pour 2 to 1
    ]

    for state in states:
        if state not in visited:
            visited.append(state)
            queue.append(state)
            parent.append((x, y))

if found:
    path = []
    current = goal

    while current != (-1, -1):
        path.append(current)

        index = 0
        while visited[index] != current:
            index += 1

        current = parent[index]

    print("Solution Path:")

    for i in range(len(path)-1, -1, -1):
        print(path[i])

else:
    print("Target cannot be measured")
