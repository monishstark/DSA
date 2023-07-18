def func(n,q):
    
    occ=set()
    used=set()
    
    for i in q:
        if i not in occ and n>0:
            occ.add(i)
            n-=1
        elif i in occ:
            occ.remove(i)
            n+=1
            used.add(i)
    return(len(set(q)-used))



print (func(2, "ABBAJJKZKZ"))
print (func(3, "GACCBDDBAGEE"))
print (func(3, "GACCBGDDBAEE"))
print (func(1, "ABCBCA"))
print (func(1, "ABCBCADEED"))