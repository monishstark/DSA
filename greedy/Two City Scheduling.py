costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
costs.sort(key=(lambda x:x[0]-x[1]))
n=1
mid=len(costs)//2
ans=0
for i,j in costs:
    if n<=mid:
        ans+=i
    else:
        ans+=j
    n+=1
print(ans)