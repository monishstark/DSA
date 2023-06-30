rank={i:0 for i in range(1,8)}
parent={i:i for i in range(1,8)}


def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]


def union(u,v):
    uu=find(u)
    uv=find(v)
    
    if uu==uv:
        return
    
    if rank[uu]<rank[uv]:
        parent[uu]=uv
    elif rank[uv]<rank[uu]:
        parent[uv]=uu
    else:
        rank[uu]+=1
        parent[uv]=uu

q=[[1,2],[2,3],[4,5],[6,7],[5,6],[3,7]]

for i,j in q:
    union(i,j)
    print(*rank.values())
    print(*parent.values())

print(rank)
print(parent)
print(find(2))
print(parent)