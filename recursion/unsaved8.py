def func(pos,s,temp):
    if pos==len(s):
        if temp and temp[0] in ("a","e","i","o","u") and temp[-1] not in ("a","e","i","o","u"):
            if temp not in ans:
                ans.append(temp[:])
        return
    func(pos+1,s,temp)
    func(pos+1,s,temp+s[pos])

s="abc"
ans=[]
func(0,s,"")
print(ans)