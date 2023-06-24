def func(s,count,k,t):
    if not s:
        print(t)
        return
    for i in range(len(s)):
        if s[i] in ("a","e","i","o","u"):
            count[0]+=1
        print(count,s,s[i])
        if count[0]==k:
            count[0]=0
            func(s[i+1:],count,k,t+[s[:i]])
            




s="babylonian"
k=2
count=[0]
func(s,count,k,[])