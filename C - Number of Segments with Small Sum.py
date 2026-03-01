n,k=map(int,input().split())
a=list(map(int,input().split()))
segment,l,current=0,0,0
for r in range(n):
    current+=a[r]
    while current>k:
        current-=a[l]
        l+=1
    segment+=r-l+1
print(segment)