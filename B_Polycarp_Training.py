n=int(input())
arr=sorted(map(int,input().split()))
day=0
check,i=1,0
while i<n:
    while i<n and check>arr[i]:
        i+=1
    if i<n and arr[i]>=check:
        day+=1
        check+=1
        i+=1
   
print(day)