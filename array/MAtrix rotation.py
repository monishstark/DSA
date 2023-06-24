matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
temp=[[0 for i in range(len(matrix))]for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        temp[j][i]=matrix[i][j]
print(temp,len(matrix)//2)
for i in range(len(matrix)):
    for j in range(len(matrix)//2):
        print(i,j)
        temp[i][j],temp[i][len(matrix)-j-1]=temp[i][len(matrix)-j-1],temp[i][j]
print(temp)