s="001110010"
from collections import Counter
l=0
count=0
c0=0
c1=0
for i in range(len(s)):
    if s[i]=="0":
        c0+=1
    else:
        c1+=1
    if c0==c1:
        c0=0
        c1=0
        count+=1
print(count,l,len(s))
        
    
    