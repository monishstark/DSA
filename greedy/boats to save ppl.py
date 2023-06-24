people = [3,2,2,1]
limit = 3
count=0
i=0
j=len(people)-1
people.sort()
while i<=j:
    count+=1
    print(people[i],people[j])
    if people[i]+people[j]<=limit:
        i+=1
    j-=1
print(count)