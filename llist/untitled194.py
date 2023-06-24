a=[[1,4,20],[2,1,10],[3,2,40],[4,2,30]]

a.sort(key=lambda x:x[2],reverse=True)
time=0
sum1=0
for j,i,k in a:
    if time<i:
        time+=1
        sum1+=k
print(sum1)
        
        