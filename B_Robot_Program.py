for _ in range(int(input())):
    n,x,k=map(int,input().split())
    s=input()
    first_zero=-1
    for i in range(min(n,k)):
        if s[i]=="L":
            x-=1    
        else:
            x+=1
        if x==0:
            first_zero=i+1
            break
    if first_zero==-1:
        print(0)
        continue
          
    first_cycle_zero=-1
    k-=first_zero
    ans=1
    for i in range(min(n,k)):
        if s[i]=="L":
            x-=1
        else:
            x+=1
        if x==0:
            first_cycle_zero=i+1
            break
    if first_cycle_zero!=-1:
        ans+=k//first_cycle_zero
    print(ans)
            
        