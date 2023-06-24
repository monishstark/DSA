a=[4 ,4 ,1 ,4 ,13 ,8 ,8 ,8 ,0 ,8 ,14, 9 ,15 ,11 ,-1 ,10 ,15 ,22 ,22 ,22 ,22 ,22 ,21]
gr={i:[] for i in range(len(a))}
for i in range(len(a)):
    gr[i].append(a[i])

dist1={i:float("inf") for i in range(len(a))}
dist2={i:float("inf") for i in range(len(a))}
s1=9
s2=2
dist1[s1]=0
dist2[s2]=0
q=[s1]

while q:
    cur=q.pop(0)
    for i in gr[cur]:
        if dist1[i]>dist1[cur]+1:
            dist1[i]=dist1[cur]+1
            q.append(i)
q=[s2]
while q:
    cur=q.pop(0)
    for i in gr[cur]:
        if dist2[i]>dist2[cur]+1:
            dist2[i]=dist2[cur]+1
            q.append(i)
ans=-1
min1=float("inf")
for i in range(len(a)):
    if dist1[i]!=float("inf") and dist2[i]!=float("inf") :
        if abs(dist1[i]-dist2[i])<min1:
            min1=abs(dist1[i]-dist2[i])
            ans=i
print(ans)
            