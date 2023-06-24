nums = [1,2,2,3,3,4,4,8,8]
l=0
r=len(nums)-1
while l<r:
    mid=(l+r)//2
    if mid%2==1:
        mid-=1
    if nums[mid]!=nums[mid+1]:
        r=mid
    else:
        l=mid+2
print(nums[l])        
#test
