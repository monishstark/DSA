a=[900, 940, 950, 1100, 1500, 1800]
d=[910, 1200, 1120, 1130, 1900, 2000]
time=list(zip(a,d))
time.sort(key=lambda x:x[1])
heap=[time[0][1]]
import heapq
count=1
for i,j in time[1:]:
    if i<=heap[0]:
        count+=1
    else:
        heapq.heappop(heap)
    heapq.heappush(heap,j)
print(count)
        