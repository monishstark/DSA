a=3
b=4
dp=[[1 for i in range(b)]for i in range(a)]
for i in range(a):
    for j in range(b):
        if i==0 or j==0:
            continue
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[-1][-1])