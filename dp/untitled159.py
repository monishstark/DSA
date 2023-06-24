def func(n,no,sum1,temp,ans,req):
    
    if sum1==0:
        
        t=1
        for i in temp:
            t*=i
        ans[0]=max(ans[0],t)
        return
    if n<=0:
        return
   
    if sum1<0:
        return
    if sum1>=no[n-1]:
        func(n,no,sum1-no[n-1],temp+[no[n-1]],ans,req)
    func(n-1,no,sum1,temp,ans,req)
n=10
ans=[float('-inf')]
no=[i for i in range(1,n)]
print(no)
sum1=sum(no)
func(len(no),no,sum1,[],ans,n)
print(ans)