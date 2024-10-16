def hm(a, b):
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return b * i

a, b = map(int, input().split())

if max(a,b) == a:
    tmp = a
    a = b
    b = tmp

print(hm(a,b))