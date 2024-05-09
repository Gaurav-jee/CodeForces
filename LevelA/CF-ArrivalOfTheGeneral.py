t = int(input())

soldiersQ = list(map(int, input().split(" ")))
totalSoldiersInQueue = len(soldiersQ)
res = 0

# print(soldiersQ)

maxIndex = soldiersQ.index(max(soldiersQ))
minIndex = soldiersQ.index(min(soldiersQ))

#solving for duplication
reversedSoldierQ = soldiersQ[::-1]
# print(reversedSoldierQ)
minIndexReversed = reversedSoldierQ.index(min(soldiersQ))
# print("min from reversed Q", minIndexReversed)
# print("new min index from the Q:", totalSoldiersInQueue - 1 - minIndexReversed)
newMinIndexPostReveral = totalSoldiersInQueue - 1 - minIndexReversed

if newMinIndexPostReveral != minIndex:
    minIndex = newMinIndexPostReveral

# print(minIndex, maxIndex)

if minIndex > maxIndex:
    res += abs(0 - maxIndex) + abs(totalSoldiersInQueue - 1 - minIndex)
else:
    res += abs(0 - maxIndex) + abs(totalSoldiersInQueue - 1 - minIndex) - 1 

print(res)