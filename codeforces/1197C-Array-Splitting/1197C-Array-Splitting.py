import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = list(map(int, input_data[2:]))
    
    total_cost = a[n-1] - a[0]
    
    diffs = []
    for i in range(n - 1):
        diffs.append(a[i+1] - a[i])
    
    diffs.sort(reverse=True)
    
    
    for i in range(k - 1):
        total_cost -= diffs[i]
        
    print(total_cost)

solve()