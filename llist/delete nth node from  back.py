class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert(root,val):
    newnode=node(val)
    newnode.next=root
    root=newnode
    return root


root=None
for i in range(1,6):
    root=insert(root,i)

n=2
fast=root
for i in range(n):
    fast=fast.next
slow=root
while fast.next:
    fast=fast.next
    slow=slow.next

slow.next=slow.next.next
