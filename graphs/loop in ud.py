def func(pos,visted,adj,parent):
    visted.add(pos)
    for i in adj[pos]:
        if i not in visted:
            if func(i,visted,adj,pos):
                return True
        elif parent!=i:
            return True
    return False
            
adj = [[], [2], [1, 3], [2]]
visted=set()
for i in range(len(adj)):
    if i not in visted:
        if func(i,visted,adj,-1):
            print(True)