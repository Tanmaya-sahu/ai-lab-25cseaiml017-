
# Hill Climbing

n = int(input("Enter number of states: "))

graph = [[] for i in range(n)]
h = [0] * n

for i in range(n):
    h[i] = int(input("Enter heuristic of state " + str(i) + ": "))

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter source: "))
    v = int(input("Enter destination: "))

    graph[u].append(v)
    graph[v].append(u)

current = int(input("Enter starting state: "))

print("Hill Climbing Path:")

while True:
    print(current, end=" ")

    best = current

    for neighbor in graph[current]:
        if h[neighbor] > h[best]:
            best = neighbor

    if best == current:
        break

    current = best

print("\nFinal State:", current)
print("Final Heuristic:", h[current])
