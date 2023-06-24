edge=[[0,1,2],[0,4,1],[4,5,4]
,[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
n=6
adj=[[]for i in range(n)]
for i,j,k in edge:
    adj[i].append([j,k])
print(adj)
dist=[float('inf') for i in range(n)]
dist[0]=0
print(dist)
heap=[(0,0)]
import heapq
while heap:
    
    di,cur=heapq.heappop(heap)
    for i,j in adj[cur]:
        
        if dist[i]>dist[cur]+j:
            dist[i]=dist[cur]+j
            heapq.heappush(heap, (j,i))
print(dist)