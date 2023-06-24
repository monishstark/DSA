def func(n,a,d,l,r,temp):
    #print(l,r,temp)
    if abs(l-r)==d:
        print(temp)
        return
    
    if n<=0:
        return
    if l>=a[n-1]:
        func(n-1,a,d,l-a[n-1],r+a[n-1],temp+[a[n-1]])
    func(n-1, a, d, l, r, temp)

a=[1, 1, 1, 1]
d=0
temp2=a[:]
func(len(a),a,d,sum(a),0,[])