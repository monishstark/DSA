arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
dp=[1 for i in range(len(arr))]

for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j]:
            if dp[i]<dp[j]+1:
                dp[i]=dp[j]+1

maxLength = max(dp)
index = dp.index(maxLength)
result = []
for i in range(index, -1, -1):
    if dp[i] == maxLength and (not result or arr[i] < result[-1]):
        result.append(arr[i])
        maxLength -= 1
print(result)