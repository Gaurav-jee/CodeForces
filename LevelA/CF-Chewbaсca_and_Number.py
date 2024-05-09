if __name__ == "__main__":
    num = input()

    res = ""
    
    for i, digit in enumerate(num):
        intDigit = int(digit)
        if i == 0 and intDigit == 9:
            res = res + str(intDigit)
            continue                           
        if intDigit >= 5:
            intDigit = 9 - intDigit
            res = res + str(intDigit)
        else:
            intDigit = int(digit)
            res = res + str(intDigit)

    print(res)