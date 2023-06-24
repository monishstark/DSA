prices = [7,6,4,3,1]
l=0
r=1
ans=0
while r<len(prices):
    if prices[l]>prices[r]:
        l=r
        r+1
    ans=max(ans,prices[r]-prices[l])
    r+=1
print(ans)