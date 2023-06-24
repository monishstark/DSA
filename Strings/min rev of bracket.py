s="}{{}}{{{"
stack=[]
count=0
for i in s:
    if i=="{":
        stack.append(i)
    else:
        if len(stack) and stack[-1]=="}":
            stack.pop()
        else:
            stack.append(i)
            
print(len(stack))

            