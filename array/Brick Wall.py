wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]

dic={}
for i in wall:
    s=0
    for j in range(len(i)):
        s+=i[j]
        if s in dic:
            dic[s]+=1
        else:
            dic[s]=1
        

    dic[s]-=1
print(dic)
