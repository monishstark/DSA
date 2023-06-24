s = "GEEKSGEEKSFOR"
a = set(s)
print(a)

i = 0
t = {}
min_len = float('inf')

for j in range(len(s)):
    if s[j] not in t:
        t[s[j]] = 0
    t[s[j]] += 1
    
    while len(t) == len(a):
        min_len = min(min_len, j-i+1)
        t[s[i]] -= 1
        if t[s[i]] == 0:
            del t[s[i]]
        i += 1

print(min_len)
