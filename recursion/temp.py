matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j],matrix[j][i]=matrix[j][i] ,matrix[i][j]
for i in matrix:
    print(i)

for i in range(len(matrix)):
    for j in range(len(matrix[0])//2):
        matrix[i][j] ,matrix[len(matrix[0] ) - 1 -j ] =matrix[len(matrix[0] ) - 1 -j] ,matrix[i][j]
print(matrix)