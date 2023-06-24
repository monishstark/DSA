def ma(a,n):
    if n<0:
        return 0
    if n==0:
        return a[0]
    pick=a[n]+ma(a,n-2)
    notpick=ma(a,n-1)
    
    return max(pick,notpick)
hval =  [2, 7, 9, 3, 1]
print(ma(hval,len(hval)-1))