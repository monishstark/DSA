def heapify(arr,n,i):
    root=i
    left=2*i+1
    right=2*i+2
    
    if left<n and arr[left]>arr[root]:
        root=left
    
    if right<n and arr[right]>arr[root]:
        root=right
        
    if root!=i:
        arr[root],arr[i]=arr[i],arr[root]
        heapify(arr,n,root)

def bheap(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    return arr

arr = [1, 3, 5, 4, 6, 13,10, 9, 8, 15, 17]
heap=bheap(arr)
print(heap)