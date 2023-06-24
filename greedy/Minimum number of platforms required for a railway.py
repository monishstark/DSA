arr=[900, 940, 950, 1100, 1500, 1800]
dep=[910, 1200, 1120, 1130, 1900, 2000]

time=[]
for i,j in zip(arr,dep):
    time.append([i,j])
time.sort(key=(lambda x:x[0]))
print(time)
heap=[]
import heapq
count=1
heapq.heappush(heap,time[0][1])
for i,j in time[1:]:
    print(heap,i,j)
    if heap[0]>=i:
        print(".")
        count+=1
    else:
        
        heapq.heappop(heap)
    heapq.heappush(heap, j)
print(count)
    
    
    