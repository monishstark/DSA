nums = [10,9,2,5,3,7,101,18]
dp=[1 for i in range(len(nums))]
for i in range(len(nums)):
    for j in range(i):
        if nums[j]<nums[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(dp)