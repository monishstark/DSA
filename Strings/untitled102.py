

txt = "batmanandrobinarebat"
pat = "bat"

n=len(txt)
m=len(pat)

f=[0]*m
i,j=1,0

while i<m:
    if pat[i]==pat[j]:
        f[i]=j+1
        i+=1
        j+=1
    elif j>0:
        j=f[j-1]
    else:
        f[i]=0
        i+=1
i,j=0,0
while i<n:
    if txt[i]==pat[j]:
        i+=1
        j+=1
        if j==m:
            print(i-m)
            j=0
    elif j>0:
        j=f[j-1]
    else:
        i+=1
        