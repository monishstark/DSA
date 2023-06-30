a="231*+9-"
st=[]
for i in a:
    if i.isdigit():
        st.append(int(i))
    else:
        s=st.pop(-1)
        f=st.pop(-1)
        
        
        if i=="+":
            st.append(f+s)
        elif i=="-":
            st.append(f-s)
        elif i=="*":
            st.append(f*s)
        else:
            st.append(f/s)

print(st)