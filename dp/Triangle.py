t= [[2],[3,4],[6,5,7],[4,1,8,3]]
dp=[[0 for i in range(len(t))]for i in range(len(t))]
for i in range(len(t)):
    for j in range(len(t[i])):
        if i==0:
            dp[i][j]=t[i][j]
            continue
        if j==0  :
            dp[i][j]=dp[i-1][j]+t[i][j]
            continue
        elif j==len(t[i])-1:
            dp[i][j]=dp[i-1][j-1]+t[i][j]
        else:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+t[i][j]
print(min(dp[-1]))