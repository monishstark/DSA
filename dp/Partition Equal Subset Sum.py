nums = [1,5,11,5]
sum1=sum(nums)//2
dp=[[False for i in range(sum1+1)]for i in range(len(nums)+1)]
for i in range(len(nums)+1):
    dp[i][0]=True

for i in range(1,len(nums)+1):
    for j in range(1,sum1+1):
        if j>=nums[i-1]:
            dp[i][j]=(dp[i-1][j] or dp[i-1][j-nums[i-1]])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[-1][-1])