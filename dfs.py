
# DFS

n = int(input("Enter number of vertices: "))

graph = [[] for i in range(n)]

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter source: "))
    v = int(input("Enter destination: "))

    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n

def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(neighbor)

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(start)
