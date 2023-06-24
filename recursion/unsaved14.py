def func(pos,dic,t,visted,count):
    if pos==t:
        count[0]+=1
        return
    visted.add(pos)
    for i in dic[pos]:
        if i not in visted:
            func(i,dic,t,visted,count)
    visted.remove(pos)
dic={1:[0,2],0:[1,2],2:[1,0],3:[0,4],4:[3]}
visted=set()
count=[0]
func(0,dic,2,visted,count)

print(count)