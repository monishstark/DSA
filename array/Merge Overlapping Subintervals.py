s = [[1,3],[2,6],[8,10],[15,18]]
s.sort()
ans=[s[0]]
for i in s[1:]:

    if ans[-1][1]<i[0]:
        ans.append(i)
    else:
        ans[-1][1]=max(ans[-1][1],i[1])
print(ans)