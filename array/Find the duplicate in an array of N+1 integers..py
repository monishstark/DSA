nums = [1,3,4,2,2]
fast=nums[0]
slow=nums[0]
while True:
    
    fast=nums[nums[fast]]
    slow=nums[slow]
    if fast==slow:
        start=nums[0]
        while start!=slow:
            slow=nums[slow]
            start=nums[start]
        print(start)
        break