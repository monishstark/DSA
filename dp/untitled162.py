def func(n,nums,sum1,count,temp):
    if sum1==0:
        print(temp)
        count[0]+=1
        return
    if sum1<0:
        return
    if n==0:
        return
    if sum1>=nums[n-1]:
        func(n,nums,sum1-nums[n-1],count,temp+[nums[n-1]])
    func(n-1,nums,sum1,count,temp)




count=[0]
nums = [1,2,3]
target = 4
func(len(nums),nums,target,count,[])