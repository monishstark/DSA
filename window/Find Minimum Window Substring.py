s = "a"
t = "a"
from collections import Counter
fret=Counter(t)
i=0
fre={}
ans=-1
min1=float('inf')
for j in range(len(s)):
    fre[s[j]]=fre.get(s[j],0)+1

    while all(fret.get(k, 0) <= fre.get(k, 0) for k in fret):
        fre[s[i]]-=1
        if j-i+1<min1:
            min1=j-i+1
            ans=s[i:j+1]
        if fre[s[i]]==0:
            del fre[s[i]]
        i+=1
print(ans)