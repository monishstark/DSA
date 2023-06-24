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
for i in range(2,0,-1):
    root=insert(root,i)
head=root

for i in range(1):
    temp=head
    last=head
    while temp.next and temp.next.next:
        last=last.next
        temp=temp.next
    print(last.data,temp.next.data)       
    temp.next.next=head
    head=temp.next
    last.next=None

while head:
    print(head.data)
    head=head.next