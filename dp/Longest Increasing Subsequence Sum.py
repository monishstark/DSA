a=[27 ,39 ,22 ,35 ,3 ,38 ,48 ,4 ,19]
ans=[i for i in a ]
t=[1 for i in a]
for i in range(len(a)):
    for j in range(i):
        if a[j]<a[i]:
           if t[i]<t[j]+1:
               ans[i]=max(ans[i],ans[j]+a[i])
               t[i]=t[j]+1

print(ans)