time = [2]
t=1

l,r=0,max(time)*t

while l<r:
    mid=(l+r)//2
    sum1=0
    for i in time:
        sum1+=mid//i
    if sum1>=t:
        r=mid
    else:
        l=mid+1
print(l)
    
    