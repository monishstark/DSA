st=[1,3,0,5,8,5]
ed=[2,4,6,7,9,9]
time=[]
for i,j in zip(st,ed):
    time.append([i,j])

time.sort(key=(lambda x:x[1]))
print(time)
count=0
last=-1
for i in time:
    if last<i[0]:
        print(i)
        count+=1
        last=i[1]
print(count)