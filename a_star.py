
# A* Search

n = int(input("Enter number of vertices: "))

cost = [[0] * n for i in range(n)]
adj = [[False] * n for i in range(n)]
h = [0] * n

for i in range(n):
    h[i] = int(input("Enter heuristic for vertex " + str(i) + ": "))

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter source: "))
    v = int(input("Enter destination: "))
    w = int(input("Enter edge cost: "))

    adj[u][v] = True
    cost[u][v] = w

    adj[v][u] = True
    cost[v][u] = w

start = int(input("Enter start vertex: "))
goal = int(input("Enter goal vertex: "))

g = [float('inf')] * n
parent = [-1] * n
closed = [False] * n

g[start] = 0

while True:
    current = -1
    best = float('inf')

    for i in range(n):
        if not closed[i] and g[i] != float('inf'):
            f = g[i] + h[i]

            if f < best:
                best = f
                current = i

    if current == -1:
        break

    if current == goal:
        break

    closed[current] = True

    for v in range(n):
        if adj[current][v] and not closed[v]:
            new_g = g[current] + cost[current][v]

            if new_g < g[v]:
                g[v] = new_g
                parent[v] = current

if g[goal] == float('inf'):
    print("No path found")
else:
    path = []
    node = goal

    while node != -1:
        path.append(node)
        node = parent[node]

    print("Shortest Path:")

    for i in range(len(path) - 1, -1, -1):
        print(path[i], end=" ")

    print("\nTotal Cost:", g[goal])
