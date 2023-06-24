target = 7
nums = [2,3,1,2,4,3]
ans=float('inf')
sum1=0
l=0
for i in range(len(nums)):
   sum1+=nums[i]
   while sum1>=target:
       ans=min(ans,i-l+1)
       sum1-=nums[l]
       l+=1
print(ans)