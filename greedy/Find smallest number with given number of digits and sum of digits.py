d=3
s=20
ans=""
for i in range(d):
    for j in range(1 if i==0 else 0,10):
        if (s-j)<=(9*(d-i-1)):
            s-=j
            ans+=str(j)
            break
print(ans)
            