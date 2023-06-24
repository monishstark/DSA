words = ["a","b","ba","bca","bda","bdca"]
words.sort(key=lambda x:len(x))
dp={}
for i in words:
    dp[i]=1
    for j in range(len(i)):
        prev=i[:j]+i[j+1:]
        if prev in dp:
            dp[i]=max(dp[i],dp[prev]+1)
print(dp)
    