nums = [4,5,6,7,0,1,2]
t = 6
l=0
r=len(nums)-1
while l<=r:
    mid=(l+r)//2
    if nums[mid]==t:
        print(mid)
        break
    if nums[l]<=nums[mid]:
        if nums[l]<=t<=nums[mid]:
            r=mid-1
        else:
            l=mid+1
    else:
        if nums[mid]<=t<=nums[r]:
            l=mid+1
        else:
            r=mid-1