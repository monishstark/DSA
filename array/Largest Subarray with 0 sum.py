a=[15,-2,2,-8,1,7,10,23]
pre={}
sum1=0
max1=0
for i in range(len(a)):
    sum1+=a[i]
    if sum1==0:
        max1=i+1
    else:
        if sum1 in pre:
            max1=max(max1,i-pre[sum1])
        else:
            pre[sum1]=i
print(max1)