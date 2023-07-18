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



acc = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
parent={i:i for i in range(len(acc))}
rank={i:0 for i in range(len(acc))}

for i in range(len(acc)):
    for j in range(i+1,len(acc)):
        for mail in acc[j][1:]:
            if mail in acc[i]:
                union(i,j,parent,rank)
dic={i:acc[i] for i in range(len(acc))}
u=set()
for i in range(len(acc)):
    p=find(i,parent)
    u.add(p)
    for j in dic[i]:
        if j not in dic[p]:
            dic[p]+=[j]
ans=[]
for i in list(u):
    ans.append([dic[i][0]]+sorted(list(set(dic[i][1:]))))
print(ans)