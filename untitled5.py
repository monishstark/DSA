
x = "abcd"
y = "xycd"
dp=[[0 for i in range(len(y)+1)]for i in range(len(x)+1)]

for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1]==y[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])