a=[-1, 2, 3]
k=5
dic={}
sum1=0
for i in range(len(a)):
    sum1+=a[i]
    dif=sum1-k
    if sum1-k in dic:
        print(i-dic[sum1-k])
        print(dic)
    dic[sum1]=i