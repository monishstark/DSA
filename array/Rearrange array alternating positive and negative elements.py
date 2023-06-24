arr = [1, 2, 3, -4, -1, 4]
pos=0
while pos<len(arr):
    if pos%2==0 and arr[pos]<0:
        pos+=1
        continue
    if pos%2!=0 and arr[pos]>=0:
        pos+=1
        continue
    if pos%2!=0 and arr[pos]<=0:
        r=pos+1
        while arr[r]<0 and r<len(arr):
            r+=1
        prev=arr[pos]
        arr[pos]=arr[r]
        
        i=pos+1
        while i<=r :
            prev,arr[i]=arr[i],prev
            i+=1
    elif pos%2==0 and arr[pos]>0:
        r=pos+1
        while arr[r]>=0 and r<len(arr)-1:
            r+=1
            print(pos,r,len(arr))
        prev=arr[pos]
        arr[pos]=arr[r]
        
        i=pos+1
        while i<=r:
            prev,arr[i]=arr[i],prev
            i+=1
    pos+=1     
print(arr)      
        