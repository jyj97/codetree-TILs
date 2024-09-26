n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

def coin(r, c):
    cc = 0
    for x in range(r, r + 3):
        for y in range(c, c + 3):
            if li[x][y] == 1:
                cc += 1

    return cc

answer = -1
for r in range(n - 2):
    for c in range(n - 2):
        tmp = coin(r, c)
        if tmp > answer:
            answer = tmp

print(answer)