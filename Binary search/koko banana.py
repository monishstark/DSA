piles = [30,11,23,4,20]
h = 6
import math
min1=float('inf')
for i in range(1,max(piles)+1):
    ans=0
    for j in piles:

        ans+=math.ceil(j/i)
    

l=1
r=max(piles)
while l<=r:
    mid=(l+r)//2
    ans=0
    for j in piles:
        ans+=math.ceil(j/mid)
        
    print(mid,ans)
    if ans<=h:
        r=mid-1
    else:
        l=mid+1
print(l)