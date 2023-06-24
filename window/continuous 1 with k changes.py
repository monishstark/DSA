nums = [0,1,1,1,0,1,1,0,1]

i=0
j=0
ans=0
cur=0
for j in range(len(nums)):
    if nums[j]==0:
        cur+=1
    while cur>1:
        if nums[i]==0:
            cur-=1
        i+=1
    ans=max(ans,j-i)
print(ans)