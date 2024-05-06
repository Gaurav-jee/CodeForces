n = int(input())

max_cap = 0
current_cap = 0

for _ in range(n):
    a, b = map(int, input().split())
    current_cap =  current_cap - a + b
    max_cap = max(max_cap,  current_cap)

print(max_cap)
