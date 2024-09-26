def dfs(x, y, score, dir):
    global answer, r, c, m
    if(x < 0 or x >= n or y < 0 or y >= n):
        return
    
    if (x == r and y == c and dir == 4):
        if answer < score:
            answer = score

        return
    

    score += li[x][y]
    end = 4 if dir == 4 else dir + 1
    for d in range(dir, end + 1):
        nx = x + m[d][0]
        ny = y + m[d][1]

        dfs(nx, ny, score, d)


m = {
    1 : (-1 ,1),
    2 : (-1, -1),
    3 : (1, -1),
    4 : (1, 1)
}


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for r in range(2, n):
    for c in range(1, n - 1):
        tmp = 0
        dfs(r, c, tmp, 1)

print(answer)