a=[10, 3, 5, 6, 2]
ans=[1 for i in range(len(a))]
pre=1
for i,j in enumerate(a):
    ans[i]*=pre
    pre*=j
print(ans)

post=1
for i in range(len(a)-1,-1,-1):
    ans[i]*=post
    post*=a[i]
print(ans)