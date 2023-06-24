a=[1,0,0,1,0,1,1]
dic={}
count=0
sum1=0
for i in a:
    if i==0:
        sum1-=1
    else:
        sum1+=1
    count+=dic.get(sum1,0)
    dic[sum1]=dic.get(sum1,0)+1
print(count)