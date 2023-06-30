
M = [4, -4, 2]
H = [4, 0, 5]
M.sort()
H.sort()
max1=0
for i,j in zip(M,H):
    max1=max(max1,abs(i-j))
print(max1)