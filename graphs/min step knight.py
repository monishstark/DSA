knightPos=[4,5]
t=[1,1]
q=[[knightPos[1]-1,knightPos[0]-1]]
N=6
dist=[[float('inf') for i in range(N)]for i in range(N)]
dist[knightPos[1]-1][knightPos[0]-1]=0	
while q:
    x,y=q.pop(0)
    for i,j in ((x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y-2),(x-1,y-2),(x+1,y+2),(x-1,y+2)):
		      if 0<=i<N and 0<=j<N:
                  
		          if dist[i][j]>dist[x][y]+1:
		                dist[i][j]=dist[x][y]+1
		                q.append([i,j])

for i in dist:
    print(i)