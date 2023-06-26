class node:
        def __init__(self,data):
            self.data=data
            self.left=None
            self.right=None


def sumofgrand(root,dic):
    sum1=0
    if root is None:
        return 0
    
    if root.left:
        sum1+=(sumofgrand(root.left.left,dic)+sumofgrand(root.left.right,dic))

    if root.right:
        sum1+=(sumofgrand(root.right.left,dic)+sumofgrand(root.right.right,dic))

    return sum1
def func(root,dic):
    if root is None:
        return 0
    if root in dic:
        return dic[root]
    
    inc=(root.data+sumofgrand(root,dic))
    exc=(func(root.left,dic)+func(root.right,dic))
    
    dic[root]=max(inc,exc)
    
    return dic[root]

root = node(1)
root.left = node(2)
root.right = node(3)
root.right.left = node(4)
root.right.right = node(5)
root.left.left = node(1)
dic={}
func(root,dic)
print(dic)