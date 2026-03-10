n,k=map(int,input().split())
a=list(map(int,input().split()))
current={}
l=0
ans=0
for i in range(n):
    if a[i] in current:
        current[a[i]]+=1
    else:
        current[a[i]]=1
    while len(current)>k:
        current[a[l]]-=1
        if current[a[l]]==0:
            del current[a[l]]
        l+=1
    ans+=(i-l+1)
print(ans)