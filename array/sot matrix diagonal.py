mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
dic={}
for i in range(len(mat)):
    for j in range(len(mat[0])):
        rev=len(mat[0])-j-1
    
        if i+rev not in dic:
            dic[i+rev]=[mat[i][j]]
        else:
            dic[i+rev].append(mat[i][j])
print(dic)
for i in dic.keys():
    dic[i].sort()
for i in range(len(mat)):
    for j in range(len(mat[0])):
        rev=len(mat[0])-j-1
        mat[i][j]=dic[i+rev].pop(0)
for i in mat:
    print(i)
        
    