def func(pos,a,sum1,t):
    if sum1 == 0:
        print(t)
        return
    if sum1<0:
        return
    for i in range(pos,len(a)):
        func(i+1,a,sum1-a[i],t+[a[i]])


a=[1, 5, 11, 5]
sum1=sum(a)//2
func(0,a,sum1,[])