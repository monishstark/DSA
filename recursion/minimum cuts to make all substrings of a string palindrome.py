def func(s,temp,ans):
    if not s:
        if len(temp)>0:
            ans[0]=min(ans[0],len(temp)-1)
        return
    for i in range(1,len(s)+1):
        t=s[:i]
        if t==t[::-1]:
            func(s[i:],temp+[t],ans)
        
    

s = "aab"
ans=[float('inf')]
func(s,[],ans)
print(ans)