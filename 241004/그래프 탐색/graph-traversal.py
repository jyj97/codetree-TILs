n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)



def dfs(v):
    visited[v] = True
    count = 1

    for i in graph[v]:
        if not visited[i]:
            count += dfs(i)
    
    return count

answer = dfs(1) - 1
print(answer)