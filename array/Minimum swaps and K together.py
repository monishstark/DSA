
arr = [7, 9, 5, 1, 2, 3, 8, 4, 6]
k = 5
count=0
for i in arr:
    if i<=k:
        count+=1

greater=0
for i in arr[:count]:   
    if i>k:
        greater+=1
print(count,greater)
j=count
ans=greater
for i in range(len(arr)-j):
    if arr[i]>k:
        greater-=1
    if arr[j]>k:
        greater+=1
    
    ans=min(ans,greater)
    j+=1
print(ans)
        