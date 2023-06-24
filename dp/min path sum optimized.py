grid = [[9,4,9,9],[6,7,6,4],
[8,3,3,7],[7,4,9,10]]
dp=[[float('inf') for i in range(len(grid[0]))]for i in range(len(grid))]
dp[0][0]=grid[0][0]
heap=[(0,(0,0))]
import heapq
while heap:
    dist,pos=heapq.heappop(heap)
    x,y=pos
    for i,j in ((x+1,y),(x,y+1),(x-1,y),(x,y-1)):
        if 0<=i<len(grid) and 0<=j<len(grid[0]):
            if dp[i][j]>dp[x][y]+grid[i][j]:
                dp[i][j]=dp[x][y]+grid[i][j]
                heapq.heappush(heap, (dp[i][j],(i,j)))

for i in dp:
    print(i)
    