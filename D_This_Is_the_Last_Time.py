for _ in range(int(input())):
    length,coin=map(int,input().split())
    arr=[tuple(map(int,input().split())) for _ in range(length)]
    arr.sort()
    for l,r,real in arr:
        if coin>=l and coin<=r:
            coin=max(coin,real)
    print(coin)
    