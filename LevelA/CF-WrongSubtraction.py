n, k = map(int, input().split())

n = str(n)
for _ in range(k):
    n = str(n)
    # print(n[-1])
    if n[-1] == "0":
        n = int(n)//10
    else:
        n = int(n)
        n = n-1

print(n)