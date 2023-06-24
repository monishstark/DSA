coins = [1,2,5]
am = 11
dp=[[float('inf') for i in range(am+1)]for i in range(len(coins)+1)]
for i in range(len(coins)+1):
    for j in range(am+1):
        if i ==0:
            continue
        elif j==0:
            dp[i][j]=0
        elif j>=coins[i-1]:
    
            dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i-1]]+1)
        else:
            dp[i][j]=dp[i-1][j]
print(dp)