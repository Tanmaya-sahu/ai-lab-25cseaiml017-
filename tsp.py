
# Travelling Salesman Problem (TSP)

n = int(input("Enter number of cities: "))

cost = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            cost[i][j] = 0
        else:
            cost[i][j] = int(input(
                "Cost from city " + str(i) +
                " to city " + str(j) + ": "
            ))

visited = [False] * n
path = [0] * (n + 1)
best_path = [0] * (n + 1)

best_cost = [float('inf')]

visited[0] = True
path[0] = 0

def tsp(city, count, total):
    if count == n:
        if cost[city][0] > 0:
            final_cost = total + cost[city][0]

            if final_cost < best_cost[0]:
                best_cost[0] = final_cost

                for i in range(n):
                    best_path[i] = path[i]

                best_path[n] = 0

        return

    for next_city in range(n):
        if not visited[next_city] and cost[city][next_city] > 0:
            visited[next_city] = True
            path[count] = next_city

            tsp(next_city, count + 1,
                total + cost[city][next_city])

            visited[next_city] = False

tsp(0, 1, 0)

if best_cost[0] == float('inf'):
    print("No complete tour exists")
else:
    print("Minimum Cost Tour:")

    for i in range(n + 1):
        print(best_path[i], end=" ")

    print("\nMinimum Cost:", best_cost[0])
