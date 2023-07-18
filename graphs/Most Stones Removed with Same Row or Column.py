
def find(x,parent):
    if x!=parent[x]:
        parent[x]=find(parent[x],parent)
    return parent[x]

def union(u,v,parent,rank):
    uu=find(u,parent)
    uv=find(v,parent)
    
    if uu==uv:
        return
    
    if rank[uu]<rank[uv]:
        parent[uu]=uv
    elif rank[uv]<rank[uu]:
        parent[uv]=uu
    else:
        parent[uv]=uu
        rank[uu]+=1

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
maxr=0
maxc=0
for i,j in stones:
    maxr=max(maxr,i+1)
    maxc=max(maxc,j+1)

parent={i:i for i in range(maxr+maxc)}
rank={i:0 for i in range(maxr+maxc)}
for i,j in stones:
    union(i,j+maxr,parent,rank)
s=set()
for i,j in stones:
    s.add(find(i,parent))
print(len(stones)-len(s))