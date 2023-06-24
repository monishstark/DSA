a=[1, 1, 1, 1]
k=2
pre={}
count=0
for i in a:
    dif=k-i
    if dif in pre:
        count+=pre[dif]
    if i in pre:
        pre[i]+=1
    else:
        pre[i]=1
