pairs = [[1,2],[7,8],[4,5]]
pairs.sort()
dp=[1 for i in range(len(pairs))]
for i in range(len(pairs)):
    for j in range(i):
        if pairs[j][1]<pairs[i][0]:
            dp[i]=max(dp[i],dp[j]+1)
print(dp)