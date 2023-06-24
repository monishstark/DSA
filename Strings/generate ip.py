def func(s,temp,ans):
    if not s:
        
        if len(temp)==4 and int(temp[0])>0:
            ans.append(temp[:])
        
        return
    for i in range(1,len(s)+1):
        t=s[:i]
        if 0<=int(t)<=255 :
            func(s[i:],temp+[t],ans)
s="11211"
ans=[]
func(s,[],ans)
print(ans)
for i in ans:
    print(".".join(i))
    