def heapify(arr,n,i):
    root=i
    left=2*i+1
    right=2*i+2
    
    if left<n and arr[left]>arr[root]:
        root=left
    
    if right<n and arr[right]>arr[root]:
        root=right
    
    if root!=i:
        arr[i],arr[root]=arr[root],arr[i]
        heapify(arr,n,root)



def sort(a,n):
    
    for i in range(n//2-1,-1,-1):
        heapify(a,n,i)
    
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)



a=[4,1,3,9,7]

sort(a,len(a))
print(a)