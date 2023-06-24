a = [1, 4, 2, 3]
b = [2, 5, 1, 6]

c=4
import heapq
heap=[]
for i in a:
    for j in b:
        heapq.heappush(heap,i+j)
        c-=1
        if c<0:
            heapq.heappop(heap)
print(heap)
        