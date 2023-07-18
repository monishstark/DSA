
def find(x,parent):

    if x!=parent[x]:
        parent[x]=find(parent[x],parent)
    return parent[x]

def union(u,v,parent,size):
    uu=find(u,parent)
    uv=find(v,parent)
    
    if uu==uv:
        return
    
    if size[uu]<size[uv]:
        parent[uu]=uv
        size[uv]+=size[uu]
    else:
        parent[uv]=uu
        size[uu]+=size[uv]


def func(i,j,visted,a,parent,size):
    
    for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
        if (x,y) not in visted and  0<=x<len(a) and 0<=y<len(a[0]) and a[x][y]==1 :
            
            visted.add((x,y))
            p=len(a[0])*i+j
            c=len(a[0])*x+y
            
            union(p,c,parent,size)

            func(x,y,visted,a,parent,size)


a=[[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[0,0,1,0,0],[0,0,1,1,1],[0,0,1,1,1]]
parent={i:i for i in range(len(a)*len(a))}
size={i:1 for i in range(len(a)*len(a))}
visted=set()
count=0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==1 and (i,j) not in visted:
            func(i,j,visted,a,parent,size)
        else:
            count+=1

max1=0    

    
for i in range(len(a)):
    for j in range(len(a[0])):
        sum1=0
        visted=set()
        if a[i][j]==0:
            left=j-1
            right=j+1
            up=i-1
            down=i+1
            
            if left>=0 and a[i][left]==1:
                p=find(i*len(a[0])+left,parent)
                print(size[p],"l")
                if p not in visted:
                    visted.add(p)    
                    sum1+=size[p]
            if right<len(a[0]) and a[i][right]==1:
                p=find(i*len(a[0])+right,parent)
                print(size[p],"r")
                if p not in visted:
                    visted.add(p)    
                    sum1+=size[p]
            if 0<=up and a[up][j]==1:
                p=find(up*len(a[0])+j,parent)
                print(size[p],"u")
                if p not in visted:
                    visted.add(p)    
                    sum1+=size[p]
            if down<len(a) and a[down][j]==1:
                p=find(down*len(a[0])+j,parent)
                print(size[p],"d")
                if p not in visted:
                    visted.add(p)    
                    sum1+=size[p]
        print("......")
        max1=max(max1,sum1)
print(max1)
                
                
                
                
                
                


