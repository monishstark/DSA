grid = [[1,0,1],[1,1,0],[1,0,0]]
q=[]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            q.append((i,j,0))
ans=[[float('inf') for i in range(len(grid[0]))]for i in range(len(grid))]
visted=set()
while q:
    i,j,count =q.pop(0)
    if 0<=i<len(grid) and 0<=j<len(grid[0]) and (i,j) not in visted:
        visted.add((i,j))
        if grid[i][j]==0:
            ans[i][j]=min(ans[i][j],count)
        for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
            q.append((x,y,count+1))

for i in ans:
    print(i)        
    
    