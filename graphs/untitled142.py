def func(pos,visted,d):
    for i in range(len(d[pos])):
        if i not in visted and d[pos][i]==1:
            visted.add(pos)
            func(i,visted,d)
            
            
            
d = [[1,0,0],[0,1,0],[0,0,1]]
visted=set()
count=0
for i in range(len(d)):
    if i not in visted:
        func(i,visted,d)
        count+=1
print(count)