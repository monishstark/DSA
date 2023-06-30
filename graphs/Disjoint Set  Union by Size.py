
size={i:0 for i in range(1,8)}
parent={i:i for i in range(1,8)}

def find(x):
    if x!=parent[x]:
        parent[x]=func(parent[x])
    return parent[x]

def union(u,v):
    uu=find(u)
    uv=find(v)
    
    if uu==uv:
        return
    
    if size[uu]<size[uv]:
        parent[uu]=uv
        size[uv]+=size[uu]
    else:
        parent[uv]=uu
        size[uu]+=size[uv]



q=[[1,2],[2,3],[4,5],[6,7],[5,6],[3,7]]

for i,j in q:
    union(i,j)
    print(*size.values())
    print(*parent.values())

print(size)
print(parent)
print(find(2))
print(parent)