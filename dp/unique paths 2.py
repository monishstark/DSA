grid = [[0,1],[0,0]]
dp=[[1 for i in range(len(grid[0]))]for i in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            dp[i][j]=0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i==0 or j==0:
            continue
        if grid[i][j]==0:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[-1][-1])
            