
import heapq
a=[4,3,2,6]
heapq.heapify(a)
sum1=0
while len(a)>1:
    f=heapq.heappop(a)
    s=heapq.heappop(a)
    sum1+=(f+s)
    heapq.heappush(a,f+s)
print(sum1)