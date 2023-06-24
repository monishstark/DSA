arr = [1,2,1]
stack=[]
ans=[-1]*len(arr)
for i in range(len(arr)):
    while stack and arr[stack[-1]]<arr[i]:
        ind=stack.pop(-1)
        ans[ind]=arr[i]
    stack.append(i)

print(ans)
        