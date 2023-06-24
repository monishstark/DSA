s = "AABABBA"
k = 1
fr={}
ans=0
i=0
mfr=0
for j in range(len(s)):
    fr[s[j]]=fr.get(s[j],0)+1
    mfr=max(mfr,fr[s[j]])
    print(mfr)
    
    if mfr+k<j-i+1:
        fr[s[i]]-=1
        i+=1
    ans=max(ans,j-i+1)
print(ans)
    
    