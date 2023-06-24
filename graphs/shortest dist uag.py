edges=[[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
n=9
adj=[[]for i in range(n)]
for i,j in edges:
    adj[i].append(j)
    adj[j].append(i)
print(adj)
dist=[float('inf') for i in range(n)]
dist[0]=0
heap=[0]
import heapq
while heap:
    cur=heapq.heappop(heap)
    for i in adj[cur]:
        if dist[i]>dist[cur]+1:
            dist[i]=dist[cur]+1
            heapq.heappush(heap, i)
print(dist)