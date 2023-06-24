def func(n,v,w,W):
    if n<=0:
        return 0
    if W>=w[n-1]:
        return max(v[n-1]+func(n-1,v,w,W-w[n-1]),func(n-1,v,w,W-w[n-1]))
    return func(n-1,v,w,W)
v=[1,2,3]
w=[4,5,1]
W=4
dp=[[0 for i in range(W+1)]for i in range(len(v)+1)]

for i in range(1,len(v)+1):
    for j in range(1,W+1):
        if j>=w[i-1]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
        else:
            dp[i][j]=dp[i-1][j]
for i in dp:
    print(i)