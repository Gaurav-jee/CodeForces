Input = list(map(int, input().split(" ")))

# print(Input)

min_ = min(Input)
max_ = max(Input)

# print(min_, max_)

mid_ = sum(Input) - min_ - max_

res = (mid_ - min_) +  (max_ - mid_)
print(res)