k,n,w = map(int, input().split())

#no of bananas possible from n dollars

TotalCostofbananas = k * ((w * (w + 1)) / 2)
# print(TotalCostofbananas)

if n < TotalCostofbananas:
    print(int(TotalCostofbananas - n))
else:
    print(0)
