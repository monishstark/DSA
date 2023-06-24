a=[90, 70, 20, 80, 50]
a.sort()
n=45
i=0
j=1
while i<len(a) and j<len(a):
    dif=a[j]-a[i]
    if dif==n and i!=j:
        print(a[j],a[i])
        break
    elif dif<n:
        j+=1
    else:
        i+=1