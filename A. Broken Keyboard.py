for _ in range(int(input())):
    s=input()
    
    l,r=0,0
    st=set()
    while r<len(s):
        while r<len(s) and s[r]==s[l]:
            r+=1
            
        if (r-l)%2==1:
            st.add(s[l])
            l=r
        else:
            l=r
    print("".join(sorted(st)))
            