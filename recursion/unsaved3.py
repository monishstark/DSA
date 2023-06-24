def func(pos,a,visted):
    i,j=pos
    if 0<=i<len(a) and 0<=j<len(a[0]) and (i,j) not in visted and a[i][j]==0:
        visted.add((i,j))
        for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
            func((x,y),a,visted)
a=[[0,1,1,1,1],
   [0,0,1,0,1],
   [1,0,1,0,1],
   [1,1,0,1,1],
   [0,1,1,0,1]]
visted=set()
count=0
for i in range(len(a)):
    for j in range(len(a[0])):
        if (i,j) not in visted and a[i][j]==0:
            
            func((i,j),a,visted)
            count+=1
print(count)