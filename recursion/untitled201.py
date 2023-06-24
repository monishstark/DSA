s="banana"
dp=[[0 for i in range(len(s)+1)]for i in range(len(s)+1)]
rev=s[::-1]
for i in range(1,len(s)+1):
    for j in range(1,len(s)+1):
        if rev[i-1]==s[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(len(s)-dp[-1][-1])