n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]


dx = (1,-1,0,0)
dy = (0,0,1,-1)

def dfs(x, y):
    c = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n and 0 <= ny < n) and li[nx][ny] == 1:
            li[nx][ny] = li[x][y] + 1
            c += dfs(nx, ny)
    
    return c



answer = 0
numli = []
for r in range(n):
    for c in range(n):
        if li[r][c] == 1:
            answer += 1
            tmp = dfs(r,c)
            numli.append(tmp)


numli.sort()
print(answer)
for i in numli:
    print(i - 1)