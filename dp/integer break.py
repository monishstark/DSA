def func(n,a,sum1,temp,ans):
    if sum1==0:
        t=1
        for i in temp:
            t*=i
        ans[0]=max(ans[0],t)
        return
    if sum1<0:
        return
    if n<=0:
        return
    if sum1>=a[n-1]:
        func(n,a,sum1-a[n-1],temp+[a[n-1]],ans)
    func(n-1,a,sum1,temp,ans)


n=6
a=[i for i in range(1,n)]
ans=[float('-inf')]
func(len(a),a,n,[],ans)
print(ans)
