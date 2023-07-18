def func(pos,a,t):
    if pos==len(a):
        print(t)
        return
    for i in a[pos]:
        func(pos+1,a,t+[i])
        

a=[["you", "we"],
        ["have", "are"],
        ["sleep", "eat", "drink"]]

func(0,a,[])