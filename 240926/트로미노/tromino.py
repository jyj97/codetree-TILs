n, m = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

# 2*2 네모에서 한칸 선택해서 삭제할 경우 값들 비교하면 되지
# 아니지. 그냥 네모에서 제일 작은애 뺴주면 되지
answer = -1
for r in range(n - 1):
    for c in range(m - 1):
        tmp = [li[r][c], li[r + 1][c], li[r][c + 1], li[r + 1][c + 1]]
        tmpsum = sum(tmp) - min(tmp)

        if tmpsum > answer:
            answer = tmpsum

# 일자로 3개 중 1*3
for r in range(n):
    for c in range(m - 2):
        tmpsum = li[r][c] + li[r][c + 1] + li[r][c + 2]
        if tmpsum > answer:
            answer = tmpsum

# 3*1
for r in range(n - 2):
    for c in range(m):
        tmpsum = li[r][c] + li[r + 1][c] + li[r+2][c]
        if tmpsum > answer:
            answer = tmpsum

print(answer)