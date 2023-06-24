a=[7 ,2, 8 ,9 ,1 ,3 ,6 ,5]
stack=[]
ns=[-1]*len(a)
ps=[-1]*len(a)
for i in range(len(a)):
    while stack and a[stack[-1]]>a[i]:
        ind=stack.pop(-1)
        ns[ind]=a[i]
    if stack:
            ps[i]=a[stack[-1]]
    stack.append(i)
print(ns)
print(ps)
for i in range(len(a)):
    cur=a[i]
    w=ns[i]-ps[i]-1
    print(cur*w)
