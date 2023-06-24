a=[[0,1,5],[1,2,3],[0,2,1]]
dic={i:[] for i in range(3)}

for i,j,k in a:
    dic[i].append([j,k])
    dic[j].append([i,k])
dist={i:float('inf') for i in range(3)}
q=[[0,0]]
visted=set()
ans=0
dist[0]=0
import heapq
while q:
    d,cur=heapq.heappop(q)
    if cur in visted:
        continue
    visted.add(cur)
    ans+=d
    for i,j in dic[cur]:
        if dist[i]>dist[cur]+j:
            dist[i]=dist[cur]+j
            heapq.heappush(q,[j,i])
            
print(ans)