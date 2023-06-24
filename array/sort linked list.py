class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert(root,val):
    newnode=node(val)
    newnode.next=root
    root=newnode
    return root

def ms(l1,l2):
    if l1 is None or l2 is None:
        return l1 or l2
    dummy=prev=node(-1)
    while l1 and l2:
        if l1.data<=l2.data:
            prev.next=l1
            l1=l1.next
        else:
            prev.next=l2
            l2=l2.next
        prev=prev.next
    prev.next=l1 or l2
    return dummy.next

def func(root):
    if root is None or root.next is None:
        return root
    slow=root
    fast=root.next
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    right=slow.next
    slow.next=None
    l=func(root)
    r=func(right)
    
    return ms(l,r)
root=None
root=insert(root,5)
root=insert(root,1)
root=insert(root,4)
root=insert(root,3)
root=insert(root,2)

root=func(root)
while root:
    print(root.data)
    root=root.next

