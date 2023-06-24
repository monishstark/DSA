a=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
max1=count=prev=0
for i,j in enumerate(a[:len(a)-1]):
    max1=max(max1,j+i)
    if max1<=i:
        print("no")
        break
    if i==prev:
        count+=1
        prev=max1
print(count)