class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def func(pre):
    if not pre:
        return None
    root=node(pre[0])
    i=1
    while i<len(pre) and pre[i]<root.data:
        i+=1
    root.left=func(pre[1:i])
    root.right=func(pre[i:])
    return root
pre=[8,5,1,7,10,12]
root=None
func(pre)
