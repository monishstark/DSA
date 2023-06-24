nums = [100,4,200,1,3,2]
temp=set(nums)
ans=0
for i in nums:
    
    if i-1 not in temp:
        count=0
        val=i
        while val in temp:
            val+=1
            count+=1
        ans=max(ans,count)
print(ans)
    