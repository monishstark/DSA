
grid = [[0,2]]

fresh=[]
rotten=[]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==2:
            rotten.append((i,j))
        elif grid[i][j]==1:
            fresh.append((i,j))
time=0
while fresh and rotten:
    n=len(rotten)
    for _ in range(n):
        i,j=rotten.pop(0)
        for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
            if (x,y) in fresh:
                fresh.remove((x,y))
                rotten.append((x,y))
    time+=1
print(time)