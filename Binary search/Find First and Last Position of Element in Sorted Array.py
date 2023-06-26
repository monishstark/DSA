nums = [5,7,7,8,8,10]
target = 8
l=0
r=len(nums)-1

while l<=r:
    mid=(l+r)//2
    if nums[mid]==target:
        st=mid
        en=mid
        while st>-1 and nums[st]==target :
            st-=1
        
        while en<len(nums) and nums[en]==target:
            en+=1
        
        print([st+1,en-1])
        break
            
    
    if nums[mid]<target:
        l=mid+1
    else:
        r=mid-1