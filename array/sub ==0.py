a=[15,-2,2,-8,1,7,10,23]
sum1=0
ans=0
dic={}
for i in range(len(a)):
    sum1+=a[i]
    if sum1==0:
        ans =i+1
    print(dic,sum1)
    if sum1 in dic:
        ans=max(ans,i-dic[sum1])
    if sum1 not in dic:
        dic[sum1]=i

print(ans)