a,b = map(int, input().split())

currentYearsNeeded = 0

for i in range(1, 99):
    # print(f"For year: {i}")
    a = a * 3
    # print(f"limak year:{i}", a)
    b = b * 2
    # print(f"Bob year:{i}", b)
    if a > b:
        print(i)
        break