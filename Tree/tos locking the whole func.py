#locking the whole func
import threading 
class Node:
    def __init__(self,val):
        self.val=val
        self.c=[]
        self.parent=None
        self.id=None
        self.locked=None
        self.deslocked=0
        self.synclock=threading.Lock()
        

def lock(node,id):

    if node.locked or node.deslocked>0:
        
        return False
    
    temp=node.parent
    while temp:
        if temp.locked:
            
            return False
        temp=temp.parent
    
    temp=node.parent
    while temp:
        temp.deslocked+=1
        temp=temp.parent
    
    
    
    node.locked=True
    node.id=id

    return True

    
    
import time
import threading   

n = 7
m = 2

nodes = ['World', 'Asia','Africa', 'China','India', 'SouthAfrica', 'Egypt']
queries =['1 China 9', '1 India 9', '3 Asia 9', '2 India 9', '2 Asia 9']
dic={}
root=Node(nodes[0])
dic[nodes[0]]=root
q=nodes[1:]
n=[root]

while q:
    parent=n.pop(0)
    for i in range(m):
        if q:
            ele=q.pop(0)
            nele=Node(ele)
            dic[ele]=nele
            nele.parent=parent
            n.append(nele)
            parent.c.append(nele)



def hlock(node,id):
    node.synclock.acquire()
    r=lock(node,i)
    node.synclock.release()
    return r   

            
print(hlock(dic["India"], 1))
print(hlock(dic["World"], 1))