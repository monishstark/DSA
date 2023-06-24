matrix = [[1,1,1],[1,0,1],[1,1,1]]
stack=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            stack.append((i,j))    
vistedr=set()
vistedc=set()
while stack:
    i,j=stack.pop(0)

    if j not in vistedc:
        vistedc.add(j)
        for x in range(len(matrix)):
            matrix[x][j]=0
    if i not in vistedr:
        vistedr.add(i)
        for y in range(len(matrix[0])):
            matrix[i][y]=0

for i in matrix:
    print(i)    