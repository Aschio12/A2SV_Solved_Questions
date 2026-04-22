for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))

    pa,mpa=0,0
    for i in range(n):
        pa+=a[i]
        mpa=max(mpa,pa)

    pb,mpb=0,0
    for i in range(m):
        pb+=b[i]
        mpb=max(mpb,pb)
    print(mpa+mpb)