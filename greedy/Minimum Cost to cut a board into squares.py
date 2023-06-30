x = [1,1,1]
y = [1,1,1]

x.sort(reverse=True)
y.sort(reverse=True)
xc=1
yc=1
ans=0
for i in range(len(x)+len(y)):
    if x and (not y or x[0]>=y[0]):
        cur=x.pop(0)
        ans+=yc*cur
        xc+=1
    elif y and (not x or y[0]>=x[0]):
        cur=y.pop(0)
        ans+=xc*cur
        yc+=1

print(ans)
            

