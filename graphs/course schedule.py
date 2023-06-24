def func(pos,gr,visted,path):
    visted.add(pos)
    path.add(pos)
    for i in gr[pos]:
        if i not in visted:
            if func(i,gr,visted,path):
                return True
        elif i in path:
            return True
    path.remove(pos)
    return False
s=[[1,0],[2,1],[3,2]]

n=4
gr=[[]for i in range(n) ]
for i,j in s:
    gr[j].append(i)
print(gr)
path=set()
visted=set()
for i in range(n):
    if i not in visted:
        if func(i,gr,visted,path):
            print("Nope")
