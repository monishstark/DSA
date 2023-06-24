class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None



root=node(10)
root.left=node(20)
root.right=node(30)
root.left.left=node(40)
root.right.right=node(100)

dic={}
min1=max1=0
q=[[root,0]]
while q:
    node,dist=q.pop(0)
    if dist not in dic:
        dic[dist]=node.val
    if node.left:
        q.append([node.left,dist-1])
    if node.right:
        q.append([node.right,dist+1])
    min1=min(min1,dist)
    max1=max(max1,dist)

for i in range(min1,max1+1):
    print(dic[i])
