grid = [[1,2,3],[4,5,6]]
dp=[[0 for i in range(len(grid[0]))]for i in range(len(grid))]

dp[0][0]=grid[0][0]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i==0 and j==0:
            continue
        if i==0:
            dp[i][j]=dp[i][j-1]+grid[i][j]
            continue
        elif j==0:
            dp[i][j]=dp[i-1][j]+grid[i][j]
            continue
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]

for i in dp:
    print(i)
            4