matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target =80

up=0
down=len(matrix)-1

while up<=down:
    mid=(up+down)//2
    if target<matrix[mid][0]:
        down=mid-1
    elif matrix[mid][-1]<target:
        up=mid+1
    else:
        break

l=0
r=len(matrix[0])-1
while l<=r:
    mid2=(l+r)//2
    if matrix[mid][mid2]==target:
        print(mid,mid2)
        break
    elif target<matrix[mid][mid2]:
        r=mid2-1
    else:
        l=mid+1