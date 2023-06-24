def fhash(s):
    val=0

    for i in s:
        val = (val * 26 + ord(i) - ord("A") + 1)

    return val

def rollhash(curhash,old,new,l):

    curhash-=(ord(old)-ord("A")+1)*(26**(l-1))
    curhash=curhash*26+(ord(new)-ord("A")+1)
    return curhash


def func(txt,pat):
    ph=fhash(pat)
    th=fhash(txt[:len(pat)])

    print(ph,th)

    for i in range(len(txt)-len(pat)+1):
        print(ph,th)
        if ph==th:
            if txt[i:i+len(pat)]==pat:
                print(i)
        if i<len(txt)-len(pat):
            th=rollhash(th,txt[i],txt[i+len(pat)],len(pat))
    return -1



txt= "HELLO"
pat = "LL"

func(txt,pat)
