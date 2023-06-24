import math
class Node:
    def __init__(self,val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.isDescendantLocked = 0


class tree:
    def __init__(self,n,m,node,q):
        self.node=[]
        self.nodemap={}
        
        for i in node:
            print(i)
            converted=Node(i)
            self.node.append(converted)
            self.nodemap[i]=converted
        
        for i in range(int(n/m)):
            start = i*m + 1
            end = i*m + m
            if end > n-1:
                end -= end%(n-1)
            if end < n:
                self.node[i].children = self.node[start: end+1]
            
        for i in range(1, n):
            self.node[i].parent = self.node[math.ceil(i/m) - 1]

        self.root = self.node[0]
        self.processed_queries = [query.split() for query in queries]
from collections import deque

def level_order(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            q.extend(node.children)
        res.append(level)
    return res
n = 7
m = 2
apis = 5
nodes = ['World', 'Asia','Africa', 'China','India', 'SouthAfrica', 'Egypt']
queries = ['1 China 9', '1 India 9', '3 Asia 9', '2 India 9', '2 Asia 9']


obj=tree(n,m,nodes,queries)
level_order_list = level_order(obj.root)
for level in level_order_list:
    print(level)