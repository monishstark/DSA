def func(n,s,t,temp):
    if t==0:
        print(temp)
        return
    if n<0:
        return
    if t<0:
        return
    if t>=s[n-1]:
        func(n,s,t-s[n-1],temp+[s[n-1]])
    func(n-1,s,t,temp)

s = [2,3,5]
t= 8
func(len(s),s,t,[])