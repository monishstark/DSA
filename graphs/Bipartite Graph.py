def func(pos,dic,color,cur):
    color[pos]=cur
    for i in dic[pos]:
        if color[i]==-1:
            if func(i,dic,color,1-cur):
                return True
        elif color[i]==cur:
            return True
    return False


dic={0:[2,3],1:[3],2:[0,3],3:[0,2,1]}

color=[-1 for i in dic.keys()]

for i in dic.keys():
    if color[i]==-1:
        if func(i,dic,color,0):
            print(False)