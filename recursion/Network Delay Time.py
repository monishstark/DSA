times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
st = 2
dic={i:[] for i in range(1,n+1)}
dist={i:float('inf') for i in range(1,n+1)}
for i,j,k in times:
    dic[i].append([j,k])
q=[st]
dist[st]=0

while q:
    cur=q.pop(0)
    for i,j in dic[cur]:
        if dist[i]>dist[cur]+j:
            dist[i]=dist[cur]+j
            q.append(i)

print(dist)
            