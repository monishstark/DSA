a=[1,2,1,3,5,6,4]
l=0
r=len(a)-1
while l<r:
    mid=(l+r)//2
    if a[mid]>a[mid+1]:
        r=mid
    else:
        l=mid+1
print(l)