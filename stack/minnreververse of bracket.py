s="[]"
count=0
stack=[]
for i in s:
    if i =="[":
        stack.append(i)
    elif stack:
        stack.pop()
    else:
        stack.append(i)
        count+=1
print(count+len(stack)//2)