

Input = list(map(int, input().split(" ")))

# print(Input)

n, k, l, c, d, p, nl, np = Input

drink_toasts = (k * l) // nl
# print(drink_toasts)
limes_toasts = c * d 
# print(limes_toasts)
salt_toasts = p // np
# print(salt_toasts)

res = min(drink_toasts, limes_toasts, salt_toasts) // n

print(res)
