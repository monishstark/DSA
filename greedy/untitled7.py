a=[1 ,2 ,3 ,4 ,5 ,6, 7 ,8 ,9 ,10]
k=1
le=len(a)-k
import heapq
minheap=[]
maxheap=[]
for i in a:
    heapq.heappush(maxheap, i)
    heapq.heappush(minheap, -i)
    
    if len(maxheap)>le:
        heapq.heappop(maxheap)
    if len(minheap)>le:
        heapq.heappop(minheap)
  
print(minheap,maxheap)
    