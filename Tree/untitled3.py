a=[(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)]
a.sort(key=lambda x:x[2])
dic={}
for i,j,k in a:
    if j not in dic:
        dic[j]=k
    else:
        dic[j]=max(dic[j],k)
