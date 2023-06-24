class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def func(root,ans):
    if root is None:
        return
    func(root.right,ans)
    ans[0]+=root.data
    root.data=ans[0]
    func(root.left,ans)
    
    

root=node(50)
root.left=node(30)
root.left.left=node(20)
root.left.right=node(40)
root.right=node(70)
root.right.left=node(60)
root.right.right=node(80)
ans=[0]
func(root,ans)
func