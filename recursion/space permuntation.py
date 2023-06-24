def func(a,t):
    if not a :
        if t[0]!=" ":
            print(t)
        return
    func(a[1:],t+a[0])
    func(a[1:],t+" "+a[0])
    


a="abc"
func(a,"")