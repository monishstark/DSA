a=[1,2,8,10,11,12,19]
x=13
l=0
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        print(mid)
        break
    if x<a[mid]:
        r=mid-1
    else:
        l=mid+1
print(l-1)