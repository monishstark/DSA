points = [[3,12],[-2,5],[-4,1]]
dic={}
for i in range(len(points)):
    for j in range(i+1,len(points)):
        
        dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        if tuple(points[i]) not in dic:
            dic[tuple(points[i])]=[[tuple(points[j]),dist]]
            
            
        else:
            dic[tuple(points[i])].append([tuple(points[j]),dist])
        
        if tuple(points[j]) not in dic:
            dic[tuple(points[j])]=[[tuple(points[i]),dist]]
            
            
        else:
            dic[tuple(points[j])].append([tuple(points[i]),dist])
print(dic)
q=[[0,tuple(points[0])]]
sum1=0
visted=set()
import heapq

while q:
    d,cur=heapq.heappop(q)
    if cur in visted:
        continue
    visted.add(cur)
    sum1+=d
    for i,j in dic[cur]:
        if i not in visted:
            heapq.heappush(q,[j,i])
print(sum1)