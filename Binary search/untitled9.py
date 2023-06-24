piles = [30, 11, 23, 4, 20]
h=5
l=0
r=max(piles)
import math
while l<=r:
    mid=(l+r)//2
    ans=0
    for i in piles:
        ans+=math.ceil(i/mid)
    print(mid,ans)
    if ans>h:
        l=mid+1
    else:
        r=mid-1
print(l)