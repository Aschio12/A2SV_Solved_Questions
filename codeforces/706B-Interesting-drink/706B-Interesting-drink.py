n=int(input())
shop=list(map(int,input().split()))
shop.sort()
for _ in range(int(input())):
    mi=int(input())
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if shop[mid]<=mi:
            l=mid+1
        else:
            r=mid-1
   
    print(l)