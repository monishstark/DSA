s=[1,3,0,5,8,5]
e=[2,4,6,7,9,9]
time=list(zip(s,e))
dp=[1]*len(time)

for i in range(len(time)):
    for j in range(i):
        if time[j][1]<time[i][0]:
            dp[i]=max(dp[i],dp[j]+1)

print(dp)