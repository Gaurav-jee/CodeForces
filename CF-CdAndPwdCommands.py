
def solution():
    stack = ['/']
    for _ in range(int(input())):
        s = input()
        if s == "pwd":
            print("".join(stack))
        else:
            if s[3]=='/':
                stack.clear()
                stack.append('/')
    
            r = s[3:].split('/')
            for i in r:
                if i=='':
                    continue
                elif i=="..":
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(i)
                    stack.append('/')

solution()