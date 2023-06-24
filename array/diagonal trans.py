mat = nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
ans={}
print(ans)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i+j in ans:
            ans[i+j].append(mat[i][j])
        else:
            ans[i+j]=[mat[i][j]]
print(ans)
re=[]
for j in ans.values():
    re+=j[::-1]
print(re)

