class node:
    def __init__(self,data):
        self.data =data
        self.next=None
def ins(root,x):
    newnode=node(x)
    newnode.next=root
    root=newnode
    return root

root=None
a=[2,2,4,5]
for i in a[::-1]:
    root=ins(root,i)
prev = None
node = root
while node:
    if prev and prev.data == node.data:
        prev.next = node.next
        node = node.next
    else:
        prev = node
        node = node.next

while root:
    print(root.data)
    root = root.next