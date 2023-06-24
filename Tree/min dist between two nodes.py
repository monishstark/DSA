class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def func(root,parent,gr):
    if root is None:
        return
    if parent !=-1:
        if parent not in gr:
            gr[parent]=[root.data]
        elif parent in gr:
            gr[parent].append(root.data)
        if root.data not in gr:
            gr[root.data]=[parent]
        elif root.data in parent:
            gr[root.data].append(parent)
    func(root.left,root.data,gr)
    func(root.right,root.data,gr)
root=node(1)
root.left=node(2)
root.right=node(3)
a=2
b=3
gr={}
func(root,-1,gr)

print(gr)
dist={i:float('inf') for i in gr}
dist[a]=0
q=[a]
while q:
    cur=q.pop(0)
    for i in gr[cur]:
        if dist[i]>dist[cur]+1:
            dist[i]=dist[cur]+1
            q.append(i)
print(dist)