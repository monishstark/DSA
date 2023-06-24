a=[4 ,4 ,1 ,4 ,13 ,8 ,8 ,8 ,0 ,8 ,14, 9 ,15 ,11 ,-1 ,10 ,15 ,22 ,22 ,22 ,22 ,22 ,21]
gr={i:[] for i in range(len(a))}
for i in range(len(a)):
    gr[i].append(a[i])

c1=9
c2=2
dist1={i:float('inf') for i in range(len(a))}
dist2={i:float('inf') for i in range(len(a))}
dist1[c1]=0
dist2[c2]=0
q=[c1]
while q:
    cur=q.pop()
    for i in gr[cur]:
        if dist1[i]>dist1[cur]+1:
            dist1[i]=dist1[cur]+1
            q.append(i)


q=[c2]
while q:
    cur=q.pop()
    for i in gr[cur]:
        if dist2[i]>dist2[cur]+1:
            dist2[i]=dist2[cur]+1
            q.append(i)

min1=float('inf')
ans=-1
for i in range(len(a)):
    if dist1[i]!=float('inf') and dist2[i]!=float('inf'):
        if min1>dist1[i]+dist2[i]:
            min1=dist1[i]+dist2[i]
            ans=i
print(ans)
