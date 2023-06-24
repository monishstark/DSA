def func(mid):
    count=0
    while mid>=5:
        mid//=5
        count+=mid
    return count
n=6
l=0
h=n*5
while l<=h:
    mid=(l+h)//2
    count=func(mid)
    if count==n:
        print(mid)
        break
    if count>n:
        r=mid-1
    else:
        l=mid+1
print(l)