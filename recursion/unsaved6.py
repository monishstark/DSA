s="abccbccba"
stack=[]
for i in s:
    if stack and stack[-1]==i:
        stack.pop(-1)
    else:
        stack.append(i)
print(stack)
