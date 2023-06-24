

a=[0,1,0,1]
dic={0:-1}
count=0
max1=0
for j,i in enumerate(a):
    print(i,dic)
    if i==0:
        count-=1
    else:
        count+=1
    
    if count in dic:
        max1=max(max1,j-dic[count])
    else:
        dic[count]=j
print(max1)