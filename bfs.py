
# BFS (Breadth First Search)

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = [False] * n
queue = [0] * n

front = 0
rear = 0

visited[start] = True
queue[rear] = start
rear += 1

print("BFS Traversal:")

while front < rear:
    current = queue[front]
    front += 1

    print(current, end=" ")

    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue[rear] = neighbor
            rear += 1
