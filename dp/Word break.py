B = [ "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream",
"man", "go", "mango" ]
A = "ilike"
B=set(B)
dp=[False]*(len(A)+1)
last=0
dp[0]=True
for i in range(1,len(A)+1):
    for j in range(i):
        if dp[j] and A[j:i] in B:
        
            dp[i]=True
            break
print(dp)