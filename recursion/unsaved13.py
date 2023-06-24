s=[2,1]
e=[2,2]
time=[]
for i,j in zip(s,e):
    time.append([i,j])
time.sort(key= lambda x:x[1])
print(time)
end=-1
count=0
for i,j in time:
    print(end,j)
    if end<i:
        end=j
        count+=1
print(count)
        