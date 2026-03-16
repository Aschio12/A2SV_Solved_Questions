for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()

    possible=[False] * n

    zero,one=0,0
    for i in range(n):
        if a[i]=="0":
            zero+=1
        else:
            one+=1
        if zero==one:
            possible[i]=True
    
    flipped=0
    for i in range(n-1,-1,-1):
        current=a[i]
        if flipped%2==1:
            current="1" if a[i]=="0" else "0"

        if current!=b[i]:
            if not possible[i]:
                print("NO")
                break
            flipped+=1
    else:
        print("YES")