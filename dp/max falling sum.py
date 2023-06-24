grid = [[348, 391],
          [618, 193]]
dp=[[0 for i in range(len(grid[0]))]for i in range(len(grid))]
for j in range(len(grid[0])):
    dp[0][j]=grid[0][j]
for i in range(1,len(grid)):
    for j in range(len(grid[0])):
        if j==0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j+1])+grid[i][j]
        elif j==len(grid[0])-1:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+grid[i][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])+grid[i][j]
ans=float('-inf')
for j in dp[len(grid)-1]:
    ans=max(ans,j)
print(ans)