n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
gr={i:[] for i in range(n)}
for i,j,p in flights:
    gr[i].append([j,p])

dist={i:[float('inf'),float('-inf')] for i in range(n)}
dist[src][0]=0
dist[src][1]=k

import heapq
q=[[src,k]]
while q:
    cur,st=heapq.heappop(q)
    
    for i,j in gr[cur]:

        if dist[i][0]>dist[cur][0]+j and st>=0:
            dist[i][0]=dist[cur][0]+j
            dist[i][1]=st
            
            heapq.heappush(q,[i,st-1])
print(dist)
            
    