def func(pos,nums,temp):
    print(temp)
    for i in range(pos,len(nums)):
        func(i+1,nums,temp+[nums[i]])
nums = [1,2,2]
func(0,nums,[])