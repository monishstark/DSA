class node:
    def __init__(self,val):
        self.val=val
        self.children=[]
        self.parent=None
        self.id=None
        self.locked=False
        self.anclocked=0
        self.deslocked=0
        
def ancchange(node,val):
    if node is None:
        return
    
    node.anclocked+=val
    for i in node.children:
        ancchange(i, val)

def lock(node,id):
    if node.locked:
        return False
    if node.anclocked>0 or node.deslocked>0:
        return False
    
    
    temp=node.parent
    while temp:
        temp.deslocked+=1
        
        temp=temp.parent
    
    ancchange(node,1)
    
    node.locked=True
    node.id=id
    return True
    
    
    
def unlock(node,id):
    
    if node.locked == False:
        
        return False
    if node.id!=id:
        
        return False
    
    
    node.locked=False
    node.id=None
    
    temp=node.parent
    while temp:
        temp.deslocked-=1
        temp=temp.parent
    
    ancchange(node, -1)
        
    return True


def update(node,id):
    if node.locked or node.anclocked>0 or node.deslocked==0:
        return False
    temp=set()
    if not(func(node,temp,id)):
        return False
    
    ancchange(node, 1)
    
    for i in temp:
        unlock(i, id)
    
    node.locked=True
    node.id=id
    return True


def func(node,a,id):
    if node is None:
        return True
    if node.locked:
        if node.id!=id:
            return False
        else:
            a.add(node)
    if node.deslocked==0:
        return True
    for i in node.children:
        if not func(i,a,id):
            return False
    
    return True
        


nodes = ["World", "China", "India"]
q=nodes[1:]
m=2
queries = ["3 India 1", "1 World 9"]
root=node(nodes[0])
n=[root]
dic={}
dic["World"]=root
print(q,1)
while q:
    parent=n.pop(0)
    
    for i in range(m):
        if q:
            print(q)
            ele=q.pop(0)
            
            nele=node(ele)
            dic[ele]=nele
            nele.parent=parent
            n.append(nele)
            parent.children.append(nele)
print(dic)
for i in queries:
    x,y,z=i.split()
    if x=="1":
        print(lock(dic[y],z))
        
    elif x=="2":
        print(unlock(dic[y],z))
        
    elif x=="3":
        print(update(dic[y],z))
        