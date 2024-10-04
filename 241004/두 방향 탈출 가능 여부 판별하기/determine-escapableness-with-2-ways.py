import sys
input = sys.stdin.readline

dx = (1, 0)
dy = (0, 1)

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):


    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n and 0 <= ny < m) and graph[nx][ny] != 0:   
            graph[nx][ny] = graph[x][y] + 1
            dfs(nx, ny)


dfs(0,0)

if graph[n - 1][m - 1] > 1:
    print(1)
else:
    print(0)