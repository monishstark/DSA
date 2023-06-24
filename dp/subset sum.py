
a=[2, 3, 5, 6, 8, 10]
sum1=10
dp=[[0 for i in range(sum1+1)]for i in range(len(a)+1)]

dp[0][0]=1
for i in range(1,len(a)+1):
    for j in range(sum1+1):
        if j>=a[i-1]:
            dp[i][j]=dp[i-1][j]+dp[i-1][j-a[i-1]]
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])