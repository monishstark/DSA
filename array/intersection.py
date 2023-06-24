f = [[0,2],[5,10],[13,23],[24,25]]
s = [[1,5],[8,12],[15,24],[25,26]]

i=0
j=0
ans=[]
while i<len(f) and j<len(s):
    
    st=max(f[i][0],s[j][0])
    end=min(f[i][1],s[j][1])
    if st<=end:
        ans.append([st,end])
    if f[i][1]<s[j][1]:
        i+=1
    else:
        j+=1
print(ans)