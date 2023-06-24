nums = [1,3,5,4,7]
dp=[1 for i in range(len(nums))]
count=[1 for i in range(len(nums))]
for i in range(len(nums)):
    for j in range(i):
        if nums[j]<nums[i]:
            if dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
                count[i]=count[j]
            elif dp[i]==dp[j]+1:
                count[i]+=count[j]
print(count)                