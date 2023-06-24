m = 3
n = 7
dp=[[1 for i in range(n)]for i in range(m)]

for i in range(1,m):
    for j in range(1,n):
        
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
print(dp)