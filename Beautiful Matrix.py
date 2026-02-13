matrix=[list(map(int,input().split())) for _ in range(5)]

def finder():
    for r in range(5):
        for c in range(5):
            if matrix[r][c]==1:
                row,col=r,c
                return (row,col)
coup=finder()
rr,cc=coup[0],coup[1]

print(abs(2-rr)+abs(2-cc))