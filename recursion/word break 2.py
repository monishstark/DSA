def func(s,temp,ans):
    if not s:
        ans.append(temp[:])
        return
    for i in range(1,len(s)+1):
        if s[:i] in dic:
            func(s[i:],temp+[s[:i]],ans)
s = "catsanddog"
dic = ["cats", "cat", "and", "sand", "dog"]
ans=[]
func(s,[],ans)
print(ans)