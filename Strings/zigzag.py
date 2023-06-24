s = "PAYPALISHIRING"
r=3
ans=[""]*r
step=1
level=0
for i in s:
    ans[level]+=i
    
    if level==0:
        step=1
    if level==r-1:
        step=-1
    level+=step
print("".join(ans))
    
    
