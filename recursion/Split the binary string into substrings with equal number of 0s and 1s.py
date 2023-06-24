from collections import Counter
def func(s,temp,ans):
    if not s:
        ans[0]=max(ans[0],len(temp))
        return
    for i in range(2,len(s)+1):
        t=s[:i]
        a=Counter(t)
        if a.get("0",0)==a.get("1",0):

            func(s[i:],temp+[t],ans)
        
        


s="0111100010"
ans=[-1]
func(s,[],ans)
print(ans[0])