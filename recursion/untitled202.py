a=[2,7,4,3,5]
stack=[]
ans=[-1]*len(a)
for i in range(len(a)):
    
    while stack and a[stack[-1]]<a[i]:
        ind=stack.pop(-1)
        ans[ind]=a[i]
    stack.append(i)

print(ans)