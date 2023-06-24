    times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

dist={i+1:float('inf') for i in range(n)}

dist[k]=0

for i in range(n-1):
    for x,y,z in times:
        if dist[x]!=float('inf') and dist[y]>dist[x]+z:
            dist[y]=dist[x]+z

#find negative weight
for x,y,z in times:
    if dist[x]!=float('inf') and dist[y]>dist[x]+z:
        print("-1")
    
    