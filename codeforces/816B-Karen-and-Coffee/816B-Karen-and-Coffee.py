#calculating the number of valid ones
for i in range(minn,maxx+1):
    p[i]=p[i-1]+prefix[i]
    
for i in range(maxx+1,m+1):
    p[i]=p[maxx]
for i in range(q):
    a,b=map(int,input().split())
    print(p[b]-p[a-1])