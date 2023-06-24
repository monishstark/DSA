a=[8,3,1,2]
sum1=0
prev=0
for i in range(len(a)):
    sum1+=a[i]
    prev+=(i*a[i])
print(sum1,prev)
ans=prev
for i in range(len(a)):
    prev=(prev-(sum1-a[i]))+(a[i]*(len(a)-1))
    print(prev)
    ans=max(ans,prev)

11-(14-8)+(8*3)
