n, m = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]


dx = (1,-1,0,0)
dy = (0,0,1,-1)

from collections import deque
def bfs(x, y):
    q = deque()

    q.append((x, y))

    while q:
        tx, ty = q.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if (0 <= nx < n and 0 <= ny < m) and li[nx][ny] == 1:
                li[nx][ny] = li[x][y] + 1

                q.append((nx, ny))


bfs(0,0)

if li[n - 1][m - 1] > 1:
    print(1)
else:
    print(0)