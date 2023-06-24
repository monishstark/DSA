def func(pos,visted,path,a):
    visted.add(pos)
    path.add(pos)
    for i in a[pos]:
        if i not in visted:
            if func(i,visted,path,a):
                return True
        elif i in path:
            return True
    path.remove(pos)
    return False
a=[[1], [2], [3], []]
visted=set()
path=set()
for i in range(len(a)):
    if i not in visted:
        if func(i,visted,path,a):
            print(True)