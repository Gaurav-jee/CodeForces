n = int(input())

arr = list(map(int, input().split()))
# print(arr)

globalMax = 0
currMax = 0

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        currMax += 1
    else:
        currMax=0
    globalMax = max(globalMax, currMax)

print(globalMax + 1)