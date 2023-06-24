s = "abciiidef"
k = 3
ans=0
count=0
from collections import Counter
for i in range(len(s)-k+1):
    temp=Counter(s[i:i+k])
    print(temp)
    if temp.get("a",0)>0 or temp.get("e",0)>0 or temp.get("i",0)>0 or temp.get("o",0)>0 or temp.get("u",0)>0:
        count=temp.get("a",0)>0+temp.get("e",0)>0+temp.get("i",0)>0+temp.get("o",0)>0+temp.get("u",0)
    ans=max(ans,count)
print(ans)