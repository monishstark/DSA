a="001"  


count0=0
expec="0"
for i in a:
    print(i,expec)
    if i!=expec:
        count0+=1
        
    if expec=="0":
        expec="1"
    else:
        expec="0"
count1=0
expec="1"
for i in a:
    print(i,expec)
    if i!=expec:
        count1+=1
    if expec=="0":
        expec="1"
    else:
        expec="0"
        
print(count0,count1)    