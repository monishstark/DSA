def func(pos,visted,stack,a):
    visted.add(pos)
    for i in a[pos]:
        if i not in visted:
            func(i,visted,stack,a)
    stack.append(pos)
a=[[], [0], [0], [0]]
visted=set()
stack=[]
for i in range(len(a)):
    if i not in visted:
        func(i,visted,stack,a)
print(stack)