for _ in range(int(input())):
    n,k=map(int,input().split())
    a=input()
    l,w=0,0
    ans=float('inf')
    for r in range(n):
        if a[r]=="W":
            w+=1
        if r-l+1==k:
            ans=min(ans,w)
        elif r-l+1>k:
            if a[l]=="W":
                w-=1
            l+=1
            ans=min(ans,w)
    print(ans)