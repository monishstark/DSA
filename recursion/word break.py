def func(a,temp,b):
    if not a:
        print(temp)
        return 
    for i in range(1,len(a)+1):
        if a[:i] in b:
            func(a[i:],temp+[a[:i]],b)
B = [ "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream",
"man", "go", "mango" ]
A = "ilikesamsung"
func(A,[],B)

    