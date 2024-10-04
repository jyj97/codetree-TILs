n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0

def dfs(a, high):
    global answer

    if visited[a]:
        return

    visited[a] = True

    if answer < high:
        answer = high

    for i in graph[a]:
        if not visited[i]:
            dfs(i, high + 1)

dfs(1, 0)
print(answer)