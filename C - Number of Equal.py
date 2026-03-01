from collections import Counter
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
aa=Counter(a)
bb=Counter(b)
for key in aa:
    if key in bb:
        count+=aa[key]*bb[key]
print(count)