class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



root=node(26)
root.left=node(10)
root.left.left=node(4)
root.left.right=node(6)

root.right=node(3)
root.right.right=node(3)

hd={}
q=[(root,0)]
while q:
    node,d=q.pop(0)
    hd[d]=node.data
    if node.left:
        q.append([node.left,d-1])
    if node.right:
        q.append([node.right,d+1])

for i,j in hd.items():
    print(i,j)
    