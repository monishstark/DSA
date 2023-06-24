e = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
s=2


dist={i:float("inf") for i in range(3)}
dist[s]=0

for x in range(3):
    for i,j,k in e:
        if dist[j]>dist[i]+k:
            dist[j]=dist[i]+k

for i,j,k in e:
    if dist[j]>dist[i]+k:
        print(1)

        