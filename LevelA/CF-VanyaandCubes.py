inputNum = int(input())

res = 0

def getNumOfcubesForLevel(level):
    return (level * (level + 1))/2


for i in range(1, 999):
    currLevelCubes = getNumOfcubesForLevel(i)
    if inputNum >= currLevelCubes:
        inputNum = inputNum - currLevelCubes
        res += 1
    if res <= 0:
        break

print(int(res))

