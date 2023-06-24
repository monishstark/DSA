nums = [3,2,4]
target = 6

dic={}
for i,j in enumerate(nums):
    
    if target-j in dic:
        print(dic[target-j],i)
    dic[j]=i