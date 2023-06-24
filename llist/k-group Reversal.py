class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert(root,x):
    newnode=node(x)
    newnode.next=root
    root=newnode
    return root
def func(head,ele):
    ele.next=head
    head=ele
    return head

root=None
for i in range(5,0,-1):
    root=insert(root,i)

dummy=prev=node(-1)
k=2
temp=root
while temp:
    t=k
    le=[]
    while t and temp:
        le.append(temp)
        temp=temp.next
        t-=1
    if t>0:

        prev.next=le[0]
        break

    head=None
    while le:
    
        
        ele=le.pop(0)
        head=func(head,ele)

    prev.next=head
    while prev.next:
        prev=prev.next
    
    

root=dummy.next
while root:
    print(root.data)
    root=root.next
        