class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def func(root,dic,parent):
    if root is None:
        return 
    if parent!=-1:
        if parent not in dic:
            dic[parent]=[root.data]
        elif parent in dic:
                dic[parent].append(root.data)
        if root.data not in dic:
            dic[root.data]=[parent]
        elif root.data in dic:
                dic[root.data].append(parent)
    func(root.left,dic,root.data)
    func(root.right,dic,root.data)
    
root=node(3)
root.left=node(5)
root.right=node(1)
root.left.left=node(6)
root.left.right=node(2)
root.left.right.left=node(7)
root.left.right.right=node(4)
root.right.left=node(0)
root.right.right=node(8)
k=2
target=5
dic={}
func(root,dic,-1)

print(dic)
dist={i:float('inf') for i in dic.keys()}
dist[target]=0
q=[target]
while q:
    cur=q.pop(0)
    for i in dic[cur]:
        
        if dist[i]>dist[cur]+1:
            dist[i]=dist[cur]+1
            q.append(i)
ans=[]
for i,j in dist.items():
    if j==k:
        ans.append(i)
print(ans)

        