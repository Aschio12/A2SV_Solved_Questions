def solve():
    # Read grid dimensions
    line1 = input().split()
    if not line1: return
    h, w = map(int, line1)
    
    grid = [input() for _ in range(h)]
    
    # 1. Identify all valid horizontal and vertical placements
    hor = [[0] * (w + 1) for _ in range(h + 1)]
    ver = [[0] * (w + 1) for _ in range(h + 1)]
    
    for r in range(h):
        for c in range(w):
            # Check for horizontal domino starting here
            if c + 1 < w and grid[r][c] == '.' and grid[r][c+1] == '.':
                hor[r+1][c+1] = 1
            # Check for vertical domino starting here
            if r + 1 < h and grid[r][c] == '.' and grid[r+1][c] == '.':
                ver[r+1][c+1] = 1
                
    # 2. Build 2D Prefix Sums for both
    prefH = [[0] * (w + 1) for _ in range(h + 1)]
    prefV = [[0] * (w + 1) for _ in range(h + 1)]
    
    for r in range(1, h + 1):
        for c in range(1, w + 1):
            prefH[r][c] = hor[r][c] + prefH[r-1][c] + prefH[r][c-1] - prefH[r-1][c-1]
            prefV[r][c] = ver[r][c] + prefV[r-1][c] + prefV[r][c-1] - prefV[r-1][c-1]
            
    # Function to get sum of a sub-rectangle in O(1)
    def get_sum(p, r1, c1, r2, c2):
        if r1 > r2 or c1 > c2:
            return 0
        return p[r2][c2] - p[r1-1][c2] - p[r2][c1-1] + p[r1-1][c1-1]

    # 3. Process Queries
    q = int(input())
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        
        # Horizontal dominos must stay within c1 to c2-1
        countH = get_sum(prefH, r1, c1, r2, c2 - 1)
        
        # Vertical dominos must stay within r1 to r2-1
        countV = get_sum(prefV, r1, c1, r2 - 1, c2)
        
        print(countH + countV)

solve()