class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def sum1(root,k,ans,t):
    
    if root is None:
        return 0
    
    if root.data==k:
        ans.append(t+[root.data])
        
    sum1(root.left,k-root.data,ans,t+[root.data])
    sum1(root.right,k-root.data,ans,t+[root.data])

def func(root,k,ans):
    if root is None:
        return
    sum1(root,k,ans,[])
    
    func(root.left,k,ans)
    func(root.right,k,ans)


root = newNode(1)
root.left = newNode(3)
root.left.left = newNode(2)
root.left.right = newNode(1)
root.left.right.left = newNode(1)
root.right = newNode(-1)
root.right.left = newNode(4)
root.right.left.left = newNode(1)
root.right.left.right = newNode(2)
root.right.right = newNode(5)
root.right.right.right = newNode(2)
 
k = 5
ans=[]
func(root,k,ans)
print(*ans)