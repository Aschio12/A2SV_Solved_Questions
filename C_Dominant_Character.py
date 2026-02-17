for _ in range(int(input())):
    n=int(input())
    s=input()
    found,a,b,c=False,0,0,0
    if "aa" in s:
        print(2)
        continue
    ans=float("inf")
    if "abbacca" in s or "accabba" in s:
        ans=7
    l=0
    
    for r in range(n):
        if s[r]=="a" and not found:
            found=True
            a+=1
            l=r
        elif found:
            if s[r]=="b":
                b+=1
            elif s[r]=="a":
                a+=1
            else:
                c+=1
            if c>a or b>a:
                found=False
                a,b,c=0,0,0
            elif a>1:
                ans=min(ans,r-l+1)
                l=r
                a-=1
                b=0
                c=0
    print(-1 if ans==float("inf") else ans)