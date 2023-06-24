def func(pos,num,target,en,prev,op,temp):
    
    if en==target:
        print(temp)
    for i in range(pos,len(num)):
        
        cur=int(num[pos:pos+i+1])
        
        func(i+1,num,target,en+cur,int(en),"+",temp+["+"]+[cur])
        func(i+1,num,target,en-cur,int(en),"-",temp+["-"]+[cur])
        func(i+1,num,target,en-prev+prev*cur,int(en),"*",temp+["*"]+[cur])
       
num = "1001"
target = 101
func(0,num,target,int(num[0]),0,"",[num[0]])