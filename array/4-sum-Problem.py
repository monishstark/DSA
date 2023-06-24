nums = [1,0,-1,0,-2,2]
target = 0
nums.sort()

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        l=j+1
        r=len(nums)-1
        while l<r:
            if nums[i]+nums[j]+nums[l]+nums[r]==target:
                print(nums[i],nums[j],nums[l],nums[r])
                l+=1
                r-=1
            if nums[i]+nums[j]+nums[l]+nums[r]<target:
                l+=1
            else:
                r-=1