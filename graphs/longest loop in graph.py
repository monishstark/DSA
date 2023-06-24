def func(pos,gr,visted,parent,le,ans):
    if  pos not in gr:
        return
    visted.add(pos)
    le+=1
    for i in gr[pos]:
        if i not in visted:
            func(i,gr,visted,pos,le,ans)
        elif i!=parent:
            ans[0]=max(ans[0],le)
    
a=[1,2,3,5,3,6,7,1]
gr={i:[] for i in range(len(a))}
for i in range(len(a)):
    gr[i].append(a[i])
ans=[0]
visted=set()
for i in range(len(a)):
    if i not in visted:
        func(i,gr,visted,-1,0,ans)
print(ans)
    