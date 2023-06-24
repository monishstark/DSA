def func(nums):
    if len(nums)>1:
        mid=len(nums)//2
        l=nums[:mid]
        r=nums[mid:]
        func(l)
        func(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                nums[k]=l[i]
                i+=1
            else:
                nums[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            nums[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            nums[k]=r[j]
            j+=1
            k+=1
        nums
        
        

nums1 = [1,2,3]
nums2 = [2,5,6]
nums1+=nums2
print(func(nums1))
print(nums1)