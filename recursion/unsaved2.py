arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
n=len(arr1)
m=len(arr2)
i = n - 1
j = m - 1
k = n + m - 1
    
while i >= 0 and j >= 0:
    print(i,j,k)
    if arr1[i] > arr2[j]:
        arr1[k] = arr1[i]
        i -= 1
    else:
        arr1[k] = arr2[j]
        j -= 1
    k -= 1
    
while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1