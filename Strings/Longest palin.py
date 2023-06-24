s = "babad"
for i in range(len(s)):
    l=i
    r=i
    while -1<l and r<len(s) and s[l]==s[r]:
        print(s[l:r+1])
        l-=1
        r+=1
    l=i
    r=i+1
    while -1<l and r<len(s) and s[l]==s[r]:
        print(s[l:r+1])
        l-=1
        r+=1    