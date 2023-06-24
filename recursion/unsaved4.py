a="[]][]["
open=0
swaps=0
for i in a:
    if i=="[":
        open+=1
    else:
        open-=1
        if open<0:
            for j in range(len(a)-1,-1,-1):
                if a[j]=="[":
                    a[j],a[j+1]=a[j+1],a[j]
                    swaps+=1
                    open+=1
                    break
print(swaps)                    
                
                
            
        