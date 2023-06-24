def func(pos,a,dp):
    
    if pos>=len(a):
        return 0
    if dp[pos]==-1:
        dp[pos]=max(a[pos]+func(pos+2,a,dp),func(pos+1,a,dp))
        return dp[pos]
    else:
        return dp[pos]
a=[1,2,3]
dp=[-1 for i in range(len(a))]
print(func(0,a,dp))