s="()(())("
stack=[-1]
ans=0
for i in range(len(s)):
    if s[i]=="(":
        stack.append(i)
    else:
        print(i,stack)
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            ans=max(ans,i-stack[-1])
print(ans)