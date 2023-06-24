a=[15,-2,2,-8,1,7,10,23]
sum1=0
ans=0
dic={}
for i ,j in enumerate(a):
    sum1+=j
    if sum1==0:
        ans=i+1
    
    if sum1 in dic:
        ans=max(ans,i-dic[sum1])
    else:
        dic[sum1]=i
print(ans)
    