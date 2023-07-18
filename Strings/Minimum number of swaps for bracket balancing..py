
s="[]][]["

count=0
close=0

for i in s:
    if i=="[":
        close-=1
    else:
        close+=1
        if close>0:
            count+=close
print(count)