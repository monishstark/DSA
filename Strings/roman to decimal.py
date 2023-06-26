
a="LXXVII"
dic= {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
ans=0

for i in range(len(a)-1):
    if dic[a[i]]<dic[a[i+1]]:
        ans-=dic[a[i]]
    else:
        ans+=dic[a[i]]
ans+=dic[a[i]]
print(ans)