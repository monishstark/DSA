class node:
    def __init__(self,data,freq,left=None,right=None):
        self.data=data
        self.freq=freq
        self.left=left
        self.right=right

def func(s,f):
    nodes=[node(i,j) for i,j in zip(s,f)]
    while len(nodes)>1:
        
        nodes.sort(key=lambda x:x.freq)
        left=nodes.pop(0)
        right=nodes.pop(0)
        nodes.append(node(None,left.freq+right.freq,left,right))
    print(nodes)
    return nodes[0]
    

def fun(root,t,dic):
    if root is None:
        return
    if root.data:
        dic[root.data]=t
        print(t)
    fun(root.left,t+"0",dic)
    fun(root.right,t+"1",dic)
    

s = "abcdef"
f= [5, 9, 12, 13, 16, 45]

root=func(s,f)
q=[root]
dic={}
fun(root,"",dic)

while q:
    level=[]
    n=len(q)
    for i in range(n):
        node=q.pop()
        level.append([node.data,node.freq])
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print(level)

print(dic)