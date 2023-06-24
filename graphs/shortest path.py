mat = [
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ] ]

dist=[[float('inf') for i in range(len(mat[0]))]for i in range(len(mat))]

dist[0][0]=0
q=[[0,(0,0)]]
import heapq
while q:
    dis,cur=heapq.heappop(q)
    x,y=cur
    
    for i,j in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        
        if 0<=i<len(mat) and 0<=j<len(mat[0]) and mat[i][j]==1:
        
            if dist[i][j]>dist[x][y]+1:
                dist[i][j]=dist[x][y]+1
                heapq.heappush(q, [dist[i][j],(i,j)])
for i in dist:
    print(i)