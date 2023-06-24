def func(s,dic,temp,ans):
    if not s:
        print(temp)
        ans[0]=True
        return
    for i in range(1,len(s)+1):
        if s[:i] in dic:
            func(s[i:],dic,temp+[s[:i]],ans)


s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
ans=[False]
func(s,wordDict,[],ans)