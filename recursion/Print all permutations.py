def func(pos,nums):
    if pos==len(nums):
        print(nums)
        return
    for i in range(pos,len(nums)):
        nums[i],nums[pos]=nums[pos],nums[i]
        func(pos+1,nums)
        nums[i],nums[pos]=nums[pos],nums[i]
        


nums = [1,2,3]
func(0,nums)