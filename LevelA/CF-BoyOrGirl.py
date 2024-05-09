UserName = input()

set_ = set()

for str in UserName:
    set_.add(str)


if len(set_)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
