class node:
    def __init__(self,val):
        self.val=val
        self.next=None

def insert(root,data):
    newnode=node(data)
    newnode.next=root
    root=newnode
    return root


root=None
a=[2,1,5]
for i in a[::-1]:
    root=insert(root,i)

a=[]
ans=[]
while root:
    a.append(root.val)
    ans.append(0)
    root=root.next
stack=[]
for i in range(len(a)):
    
    while stack and a[stack[-1]]<a[i]:
        ind=stack.pop(-1)
        ans[ind]=a[i]
    stack.append(i)

print(ans)
    
    