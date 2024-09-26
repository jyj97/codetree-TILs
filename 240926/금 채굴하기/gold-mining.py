n, m = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

def charge(k):
    return k**2 + (k+1)**2

def search(r, c, k):
    num = 0
    for x in range(r - k, r + k + 1):
        for y in range(c - k, c + k + 1):
            if 0 <= x < n and 0 <= y < n and abs(x - r) + abs(y - c) <= k and li[x][y] == 1:
                num += 1
    return num

if m >= charge(0):
    answer = 1
else:
    answer = 0

k = 1
while k <= n - 1:
    for r in range(n):
        for c in range(n):
            tmp = search(r, c, k)

            if tmp * m >= charge(k) and tmp > answer:
                answer = tmp

    k += 1

print(answer)