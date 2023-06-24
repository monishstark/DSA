

a=[[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]


ind=[0 for i in range(len(a))]
oud=[0 for i in a]
for i in range(len(a)):
    for j in range(len(a[0])):
        x=0
        if a[i][j]:
            x=1
        ind[j]+=x
        oud[i]+=x
print(ind,oud)
for i in range(len(a)):
    if ind[i]==len(a)-1  and oud[i]==0:
        print(i)