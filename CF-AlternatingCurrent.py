def solution():
    ch = input().strip()
    
    stack = []
    
    for i in range(len(ch)):
        if stack and stack[-1] == ch[i]:
            stack.pop()
        else:
            stack.append(ch[i])
            
    if not stack:
        print("Yes")
    else:
        print("No")

solution()