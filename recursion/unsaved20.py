a=[2,4,6,8,9,10,12]
b=[2,4,6,8,10,12]
i=0
j=len(a)-1
while i<=j:
    mid=(i+j)//2
    

    if mid<len(b):
        if a[mid]==b[mid]:
            i=mid+1
        else:
            j=mid-1
    else:
        j=mid-1
print(i)