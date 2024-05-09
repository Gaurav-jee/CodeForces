
friendsCount = int(input())
friends = list(map(int, input().split(" ")))

resFriendsList = [-1 for i in range(friendsCount)]
for friend in friends:
    check = friend %  friendsCount
    resFriendsList[check] = friend

print(*resFriendsList, sep=" ")