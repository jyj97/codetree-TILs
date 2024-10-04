n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


answer = 0

def dfs(a, le):
    global answer
    if visited[a]:
        return

    visited[a] = True
    le += 1
    if answer < le:
        answer = le

    for i in graph[a]:
        if not visited[i]:
            dfs(a, le)

dfs(1,1)
print(answer)