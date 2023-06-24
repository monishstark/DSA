a = "a"
b = "aa"


temp=a[:]
n=len(b)
count=1
while len(temp)<n:
    count+=1
    temp+=a
print(count)