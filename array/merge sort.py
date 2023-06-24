def func(a):
    if len(a)>1:
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        func(l)
        func(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i <len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j <len(r):
            a[k]=r[j]
            j+=1
            k+=1
        
            


a=[2, 4, 1, 3, 5]
func(a)
print(a)