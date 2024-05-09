inputString = input()

suits = set()
nums = set()

cards = list(input().split())

for card in cards:
    suits.add(card[1])
    nums.add(card[0])

resFlag = False

if inputString[0] in nums:
    resFlag = True

if inputString[1] in suits:
    resFlag = True

if resFlag == True:
    print("YES")
else:
    print("NO")