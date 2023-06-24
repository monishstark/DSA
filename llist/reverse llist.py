class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert(root,val):
    newnode=node(val)
    newnode.next=root
    root=newnode
    return root

def func(root):
    if not root or not root.next:
        return root
    a=func(root.next)
    root.next.next=root
    root.next=None
    return a

root=None
for i in range(5,0,-1):
    root=insert(root,i)

ans=func(root)

while ans:
    print(ans.data)
    ans=ans.next