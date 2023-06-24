class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


root=node(8)
root.left=node(3)
root.left.left=node(1)
root.left.right=node(6)
root.left.right.left=node(4)
root.left.right.right=node(7)
root.right=node(10)
root.right.right=node(14)
root.right.right.left=node(13)
q=[[root,(0,0)]]
temp=[[0 for i in range(6)]for i in range(6)]
dic={}
while q:
    n=len(q)
    for i in range(n):
        node,pos=q.pop(0)
        i,j=pos
        if i+j not in dic:
            dic[i+j]=[node.val]
        else:
            dic[i+j].append(node.val)
        temp[i][j]=node.val
        if node.left:
            q.append([node.left,(i+1,j)])
        if node.right:
            q.append([node.right,(i+1,j+1)])
for i in temp:
    print(i)
    