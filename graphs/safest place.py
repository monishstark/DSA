def func(pos,adj,visted,path):
    visted.add(pos)
    path.add(pos)
    for i in adj[pos]:
        if i not in visted:
            if func(i,adj,visted,path):
                return True
        elif i in path:
            return True
    path.remove(pos)
    return False
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
adj={i:[] for i in range(len(graph))}
for i in range(len(graph)):
    for j in graph[i]:
        adj[i].append(j)
print(adj)
ans=[]
loop=set()
for i in adj.keys():
    if i in loop:
        continue
    visted=set()
    path=set()
    if func(i,adj,visted,path):
        for i in visted:
            loop.add(i)
    else:
        ans.append(i)
print(ans)
            
