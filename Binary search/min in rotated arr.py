a=[10, 20, 30, 40, 50, 5, 7]
l=0
ans=float('inf')
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    ans=min(ans,a[mid])
    if a[mid]>a[r]:
        
        l=mid+1
    else:
        r=mid-1
print(ans)