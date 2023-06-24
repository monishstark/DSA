def func(s,temp):
    if not s:
        print(temp)
    for i in range(1,len(s)+1):
        t=s[:i]
        if t==t[::-1]:
            func(s[i:],temp+[t])
            

s = "aab"
func(s,[])