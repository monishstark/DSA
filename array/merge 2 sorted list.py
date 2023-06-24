nums=[1,2,3,8]
nums2=[2,5,7]
temp=nums+nums2
i=j=k=0
while i<len(nums) and j<len(nums2):
    if nums[i]<nums2[j]:
        temp[k]=nums[i]
        i+=1
    else:
        temp[k]=nums2[j]
        j+=1
    k+=1
while i<len(nums):
    temp[k]=nums[i]
    i+=1
    k+=1

while j<len(nums2):
    temp[k]=nums2[j]
    j+=1
    k+=1
print(temp)
    