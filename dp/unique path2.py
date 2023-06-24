a=[[0,0],[1,1],[0,0]]
dp=[[0 for i in range(len(a[0]))]for i in range(len(a))]
for i in range(len(a)):
    for j in range(len(a[0])):

        if a[i][j]==1:
            continue
        if i==0 and j==0 and a[i][j]==0:
            dp[i][j]=1
            continue
            
        if i==0 :
            dp[i][j]=dp[i][j-1]
        elif j==0:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i][j-1]+dp[i-1][j]
    
print(dp)    