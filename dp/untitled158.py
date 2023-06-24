def func(n,a,l,r,ans):
    if n<=0:
        return
    ans[0]=min(ans[0],abs(l-r))
    if l>=a[n-1]:
        func(n-1,a,l-a[n-1],r+a[n-1],ans)
    func(n-1,a,l,r,ans)
    
a=[1, 6, 11, 5]
l=sum(a)
ans=[float('inf')]
func(len(a),a,l,0,ans)
print(ans)