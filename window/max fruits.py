fruits = [1,2,3,2,2]
dic={}
i=0
ans=0
for j in fruits:
    dic[fruits[j]]=dic.get(fruits[j],0)+1
    while len(dic)>2:
        dic[fruits[i]]-=1
        if dic[fruits[i]]==0:
            del dic[fruits[i]]
        i+=1
    ans=max(ans,j-i+1)
print(ans)
        