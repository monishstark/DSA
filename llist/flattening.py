class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

def func(l1,l2):
    if l1 is None or l2 is None:
        return l1 or l2
    dummy=prev=Node(-1)
    while l1 and l2:
        if l1.data<=l2.data:
            prev.next=l1
            l1=l1.next
        else:
            prev.next=l2
            l2=l2.bottom
        prev=prev.next
    prev.next= l1 or l2
    return dummy.next
    

root=Node(5)
root.next=Node(10)
root.next.next=Node(19)
root.next.next.next=Node(28)

root.bottom=Node(7)
root.bottom.bottom=Node(8)
root.bottom.bottom.bottom=Node(30)

root.next.bottom=Node(20)

root.next.next.bottom=Node(22)
root.next.next.bottom.bottom=Node(50)

root.next.next.next.bottom=Node(35)
root.next.next.next.bottom.bottom=Node(40)
root.next.next.next.bottom.bottom.bottom=Node(45)

temp=root
le=[]
while temp:
    if temp.bottom:
        le.append(temp.bottom)
    temp=temp.next

for i in le:
    root=func(root,i)
while root:
    print(root.data)
    root=root.next