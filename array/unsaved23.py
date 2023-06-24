def func(a):
    if not a:
        return [""]
    ans=[]
    re=func(a[1:])
    for i in re:
        ans.append(a[0]+i)
        ans.append(a[0]+" "+i)
    return ans
a="abc"
print(func(a))