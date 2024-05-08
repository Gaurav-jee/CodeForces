t = int(input())

for _ in range(t):
    a,b,n = map(int, input().split())

    res = 0

    for i in range(n):
        if a < b:
            a += b
        elif a>=b:
            b += a
        res += 1
        if a> n or b>n:
            print(res)
            break
