class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def buildtree(ino,pre):
    if not ino:
        return 
    rootval=pre[0]
    root=node(rootval)
    root_idx=ino.index(rootval)
    leftino=ino[:root_idx]
    rightino=ino[root_idx+1:]
    leftpre=[i for i in pre if i in leftino]
    rightpre=[i for i in pre if i in rightino]
    root.left=buildtree(leftino, leftpre)
    root.right=buildtree(rightino, rightpre)
    return root

ino=[3, 1, 4 ,0 ,5 ,2]
pre=[0 ,1 ,3 ,4 ,2 ,5]
root=buildtree(ino,pre)
q=[root]
while q:
    n=len(q)
    level=[]
    for i in range(n):
        node=q.pop(0)
        level.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print(level)            