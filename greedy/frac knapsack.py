
n=3
W=50
val=[60,100]
we=[10,20]
pro=list(zip(val,we))
pro.sort(key=lambda x:x[0]/x[1],reverse=True)
print(pro)
ans=0
for i,j in pro:
    if j<=W:
        W-=j
        ans+=i
    elif W>0 :
        ans+=(i/j)*W
print(ans)
        