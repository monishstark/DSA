def func(n,nums,sum1,t,count):
    if n>len(nums):
        return 
    if n==len(nums):
        if sum1==t:
            count[0]+=1
        return
    func(n+1,nums,sum1+nums[n],t,count)
    func(n+1,nums,sum1-nums[n],t,count)
nums = [1,1,1,1,1]
t=3
count=[0]

func(0,nums,0,t,count)
print(count[0])