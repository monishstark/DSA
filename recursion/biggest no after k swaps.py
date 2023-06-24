def func(pos,s,k):
    ans[0]=max(ans[0],int("".join(s)))
    if k==0:
        return
    for i in range(pos,len(s)-1):
        for j in range(i+1,len(s)):
            if int(s[i])<int(s[j]):
                s[i],s[j]=s[j],s[i]
                func(i+1,s,k-1)
                s[i],s[j]=s[j],s[i]

s="61892795431"
s=list(s)
k=4
ans=[0]
func(0,s,k)
print(ans)