def func(r,grid,c,ld,rd,n):
    if r==n:
        for i in grid:
            print(i)
        print("111111")
        return
    for i in range(n):
        if i not in c and r-i not in ld and r+i not in rd:
            c.add(i)
            ld.add(r-i)
            rd.add(r+i)
            grid[r][i]=1
            func(r+1,grid,c,ld,rd,n)
            c.remove(i)
            ld.remove(r-i)
            rd.remove(r+i)
            grid[r][i]=0




n=4
grid=[[0 for i in range(n)]for i in range(n)]
c=set()
ld=set()
rd=set()
func(0,grid,c,ld,rd,n)