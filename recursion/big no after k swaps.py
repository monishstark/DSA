def func(pos,a,k,ans):
    if k==-1:
        return
    ans[0]=max(ans[0],int("".join(a[:])))
    for i in range(pos+1,len(a)):
        if a[pos]<a[i]:
            a[pos],a[i]=a[i],a[pos]
            func(pos+1,a,k-1,ans)
            a[pos],a[i]=a[i],a[pos]


a="1234567"
a=list(a)
ans=[0]
func(0,a,4,ans)

print(ans[0])
