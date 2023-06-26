
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def func(root,an,el,t):
    if root is None:
        return
    if el==root.data:

        if len(t)>=an:
            print(t[-an])
        else:
            print(-1)
    
    func(root.left,an,el,t+[root.data])
    func(root.right,an,el,t+[root.data])

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

func(root,2,5,[])