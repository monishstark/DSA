a=[1, 4, 45, 6, 0, 19]
t=51
e=s=0
sum1=0
min1=len(a)
while e<len(a):
    sum1+=a[e]
    while sum1>=t:
        min1=min(min1,e-s+1)
        sum1-=a[s]
        s+=1
    e+=1
print(min1)
