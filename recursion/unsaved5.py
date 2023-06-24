a="11000010001" 
maxdiff=cur=0
for i in a:
    if i=="0":
        cur+=1
    else:
        cur-=1
    if cur<0:
        cur=0
    maxdiff=max(maxdiff,cur)
print(maxdiff)