

nums = [84,-37,32,40,95]
k = 167
i=0
ans=float('inf')
sum1=0
for j in range(len(nums)):
    sum1+=nums[j]
    print(sum1)
    while sum1>=k:
        print(sum1)
        ans=min(ans,j-i+1)
        sum1-=nums[i]
        i+=1
    
print(ans)     
        