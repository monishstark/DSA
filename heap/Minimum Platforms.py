
arr = {900, 940, 950, 1100, 1500, 1800}
dep = {910, 1200, 1120, 1130, 1900, 2000}

t=[[i,j] for i,j in zip(arr,dep)]

t.sort(key=lambda x:x[0])

p=1
import heapq
q=[t[0][1]]

for i,j in t[1:]:
    
    if q[0]>=i:
        p+=1
    else:
        heapq.heappop(q)
    heapq.heappush(q,j)
print(p)