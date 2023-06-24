en = [[5,4],[6,4],[6,7],[2,3]]
en.sort()
dp=[1 for i in range(len(en))]
for i in range(len(en)):
    for j in range(i):
        if en[j][0]<en[i][0] and en[j][1]<en[i][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(dp)