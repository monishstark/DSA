nums = [3,2,1]

l=r=len(nums)-1
found=False
while 0<l:
    
    if not found:
        if nums[l-1]<nums[l]:
            found=True
        else:
            l-=1
    else:
        
        if nums[l-1]<nums[r]:
            nums[l-1],nums[r]=nums[r],nums[l-1]
            break
        else:
            r-=1
temp=nums[l:]
print(nums[:l]+temp[::-1])
    