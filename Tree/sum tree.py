class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def sum1(root):
    if root is None:
        return 0
    return root.data+sum1(root.left)+sum1(root.right)

def func(root):
    if root is None or (root.left is None and root.right is None):
        return True
    
    lsum=sum1(root.left)
    rsum=sum1(root.right)

    
    if root.data==lsum+rsum and func(root.left) and func(root.right):
        return True
    else:
        return False

root=node(26)
root.left=node(10)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(6)
root.right.right=node(3)
print(func(root))