s="abba"
f="{"
se="{"
for i in s:
    f=min(f,i)
for i in s:
    if i>f and i<se:
        se=i
print(f,se)
s=list(s)
for i,j in enumerate(s):
    if j==se:
        s[i]=f
    elif j==f:
        s[i]=se
print("".join(s))
print(min("af","ab"))
        
