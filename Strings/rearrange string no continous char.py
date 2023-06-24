s = "aaabbc"
from collections import Counter
a=Counter(s)
a=list(a.items())
print(a)
a.sort(key=lambda x:x[1],reverse=True )
print(a)
ans=[""]*len(s)
ind=0
for i,j in a:
    for k in range(j):
        if ind>=len(s):
            ind=1
        ans[ind]=i
        ind+=2
print(ans)