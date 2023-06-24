x=3
l=0
r=x
while l<=r:
    mid=(l+r)//2
    if mid**2==x:
        print(mid)
        break
    if mid**2<x:
        l=mid+1
    else:
        r=mid-1
        
print(l)