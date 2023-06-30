
class dsu:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        uu=self.find(u)
        uv=self.find(v)
        print(uu,uv)
        if uu==uv:
            return
        
        if self.rank[uu]<self.rank[uv]:
            self.parent[uu]=uv
        elif self.rank[uu]>self.rank[uv]:
            self.parent[uv]=uu
        else:
            self.parent[uv]=uu
            self.rank[uu]+=1

q=[[1,2],[2,3],[4,5],[6,7],[5,6],[3,7]]

obj=dsu(7)
for i,j in q:
    
    obj.union(i-1,j-1)
    print(obj.rank)
    print(obj.parent)
    print()
    
        