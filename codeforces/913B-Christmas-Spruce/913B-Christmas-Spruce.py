n=int(input())
d={}
for i in range(n-1):
    node=int(input())
    if node in d:
        d[node].append(i+2)
    else:
        d[node]=[i+2]

store=[]
for key in d:
    current=0
    for node in d[key]:
        if node not in d:
            current+=1
    store.append(current)
store.sort()
print("Yes" if store[0]>=3 else "No")