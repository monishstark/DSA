cells = [0,1,0,1,1,0,0,1]
n = 7
seen={}
while n>=0:
    print(cells)
    seen[tuple(cells)]=n
    n-=1
    temp=[0 for i in range(len(cells))]
    for i in range(1,len(cells)-1):
        if cells[i-1]==cells[i+1]:
            temp[i]=1
        else:
            temp[i]=0
    cells=temp
    if tuple(cells) in seen:
        n%=seen[tuple(cells)]-n
    
