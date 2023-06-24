a=[0,0,5,5,0,0]
dic={0:1}
sum1=0
count=0
for i in a:
    sum1+=i
    count+=dic.get(sum1,0)
    dic[sum1]=dic.get(sum1,0)+1
print(count)