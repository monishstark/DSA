def func(n,dp):
    if dp[n-1]==-1:
        dp[n-1]=func(n-1,dp)+func(n-2,dp)
        return dp[n-1]
    else:
        return dp[n-1]

n=1
dp=[-1 for i in range(n)]
dp[0],dp[1]=1,2
print(func(n,dp))