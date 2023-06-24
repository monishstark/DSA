a=[1, 2, 3]
low=1
high=3
l=m=0
hi=len(a)-1
while m<=hi:
    print(a,l,m,hi)
    if a[m]<low:
        print("1")
        a[m],a[l]=a[l],a[m]
        m+=1
        l+=1
    elif low<=a[m]<=high:
        print("2")
        m+=1
    elif high<a[m]:
        print("3")
        a[hi],a[m]=a[m],a[hi]
        hi-=1
print(a)