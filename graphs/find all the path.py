def func(pos,graph,visted,temp,ans):
    if pos==len(graph)-1:
        ans.append(temp+[pos])
        return
    if pos in visted:
        return
    visted.add(pos)
    for i in graph[pos]:
        func(i,graph,visted,temp+[pos],ans)
    visted.remove(pos)


graph = graph = [[4,3,1],[3,2,4],[3],[4],[]]
visted=set()
ans=[]
func(0,graph,visted,[],ans)
print(ans)