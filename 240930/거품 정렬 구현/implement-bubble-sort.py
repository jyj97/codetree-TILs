n = int(input())
li = list(map(int, input().split()))

def bubble(li):
    le = len(li)

    while True:
        sort = True
        for i in range(le - 1):
            if li[i] > li[i + 1]:
                tmp = li[i + 1]
                li[i + 1] = li[i]
                li[i] = tmp
                sort = False

        if sort:
            break

bubble(li)
for i in li:
    print(i, end = " ")