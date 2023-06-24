s = "123+*8-"
stack=[]
for i in s:
    if i not in("+","-","*","/"):
        stack.append(i)
    else:
        if i=="+":
            sec=int(stack.pop(-1))
            first=int(stack.pop(-1))
            temp=first+sec
            stack.append(temp)
        
        elif i=="-":
            sec=int(stack.pop(-1))
            first=int(stack.pop(-1))
            temp=first-sec
            stack.append(temp)
        
        elif i=="*":
            sec=int(stack.pop(-1))
            first=int(stack.pop(-1))
            temp=first*sec
            stack.append(temp)
        
        else:
            sec=int(stack.pop(-1))
            first=int(stack.pop(-1))
            temp=first/sec
            stack.append(temp)
print(stack)