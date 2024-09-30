def selective(li):
    le = len(li)

    for i in range(le - 1):
        mini = i
        for j in range(i + 1, le):
            if li[j] < li[mini]:
                mini = j
        
        tmp = li[i]
        li[i] = li[mini]
        li[mini] = tmp

n = int(input())
li = list(map(int, input().split()))

selective(li)
for i in li:
    print(i, end = " ")