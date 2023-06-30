
s1 = [4,2,3]
s2 = [1,1,2,3]
s3= [1,4]
dic={}
sum1=0
for i in s1[::-1]:
    sum1+=i
    dic[sum1]=dic.get(sum1,0)+1
sum1=0
for i in s2[::-1]:
    sum1+=i
    dic[sum1]=dic.get(sum1,0)+1
sum1=0
max1=0
for i in s3[::-1]:
    sum1+=i
    if dic.get(sum1,0)==2:
        max1=max(max1,sum1)
print(max1)