a=[0,1,0,2,1]
l=m=0
h=len(a)-1
while m<=h:
    if a[m]==0:
        a[m],a[l]=a[l],a[m]
        m+=1
        l+=1
    elif a[m]==1:
        m+=1
    else:
        a[m],a[h]=a[h],a[m]
        h-=1
print(a)
        