def func(s,t):
    if not s:
        print(t)
        return
    for i in range(1,len(s)+1):
        te=s[:i]
        if te==te[::-1]:
            func(s[i:],t+[te])


s= "madam"
func(s,[])