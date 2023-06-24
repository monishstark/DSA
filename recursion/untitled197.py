a=[100, 112, 256, 349, 770]
b=[72, 86, 113, 119, 265, 445, 892]
k=7
a=a+b
heap=[]
import heapq
for i in a:
    heapq.heappush(heap, -i)
    k-=1
    if k<0:
        heapq.heappop(heap)
print(heap)    