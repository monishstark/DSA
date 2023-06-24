a= [1,2,87,87,87,2,1]
ans=[1]*len(a)

for i in range(1,len(a)):
    if a[i]>a[i-1]:
        ans[i]=ans[i-1]+1
print(ans)
for i in range(len(a)-2,-1,-1):
    if a[i]>a[i+1]:
        ans[i]=max(ans[i+1]+1,ans[i])
print(ans)