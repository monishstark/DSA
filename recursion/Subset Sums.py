def func(pos,a,sum1):
    print(sum1)
    for i in range(pos,len(a)):
        func(i+1,a,sum1+a[i])

a=[5, 2, 1]
func(0,a,0)