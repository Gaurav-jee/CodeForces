inputString = input()

nums = []

for i in inputString:
    if i != "+":
        nums.append(i)
        
nums.sort()

res = "+".join(i for i in nums)

print(res)
