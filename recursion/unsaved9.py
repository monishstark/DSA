matrix=[[10, 20 ,30, 40],
        [ 15, 25, 35, 45],
        [ 27, 29, 37, 48],
        [ 32, 33, 39, 50]]
target=37
u=0
d=len(matrix)-1
while u<=d:
    mid=(u+d)//2
    if target<matrix[mid][0]:
        d=mid-1
    elif target>matrix[mid][-1]:
        u=mid+1
    else:
        break
        
if not u<=d:
    print(0)

l=0
r=len(matrix[mid])-1
while l<=r:
    mid1=(l+r)//2
    if matrix[mid][mid1]==target:
        print(1)
    if target<matrix[mid][mid1]:
        r=mid1-1
    else:
        l=mid1+1
print(mid)
 