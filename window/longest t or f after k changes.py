y = "TFFT"
k = 1
i=0
j=0
cur=0
ans=0
while j<len(y):
    if y[j]=="F":
        cur+=1
    
    while cur>k:
        if y[i]=="F":
            cur-=1
        i+=1
    ans=max(ans,j-i)
    j+=1
print(ans)

i=0
j=0
cur=0
ans=0
while j<len(y):
    if y[j]=="T":
        cur+=1
    
    while cur>k:
        if y[i]=="T":
            cur-=1
        i+=1
    ans=max(ans,j-i)
    j+=1
print(ans)