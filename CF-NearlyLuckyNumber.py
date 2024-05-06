number = input()

isNearlyLuckyNumber = True
luckyDigits = ["4","7"]
luckyDigitsCount = 0 
isLuckyNumber = True

for digit in number:
    if digit in luckyDigits:
        luckyDigitsCount += 1
    elif digit not in luckyDigits:
        currDigit = False
        isLuckyNumber = isLuckyNumber and currDigit

if luckyDigitsCount == 7 or luckyDigitsCount == 4:
    print("YES")
else:
    print("NO")


