

num = "1432219"
k = 3
a=list(map(int,num))
stack=[]
for i in a:
    print(stack,i)
    while stack and stack[-1]>i and k>0:
        stack.pop()
        k-=1
    stack.append(i)
print(stack)
while k>0:
    stack.pop()
    k-=1
    
print(stack)

    