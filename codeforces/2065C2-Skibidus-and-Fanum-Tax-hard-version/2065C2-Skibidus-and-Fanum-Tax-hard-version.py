import bisect

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Sort b to enable binary search
    b.sort()

    for i in range(n):
        # Determine the "previous" value we must be greater than or equal to
        # For the very first element, it just has to be greater than negative infinity
        prev = -float('inf') if i == 0 else a[i-1]
        
        # Track our best (minimum) valid option for the current element
        best_choice = float('inf')
        
        # Option 1: Keep a[i] as it is (if valid)
        if a[i] >= prev:
            best_choice = a[i]
            
        # Option 2: Flip a[i] using the optimal b[j]
        # We need b[j] >= a[i] + prev
        target = a[i] + prev
        
        # bisect_left finds the index of the first element in b that is >= target
        idx = bisect.bisect_left(b, target)
        
        if idx < m: # If such a b[j] exists
            flipped_value = b[idx] - a[i]
            # Take the minimum of keeping it or flipping it
            best_choice = min(best_choice, flipped_value)
            
        # If both options were invalid, best_choice remains infinity
        if best_choice == float('inf'):
            print("NO")
            return
            
        # Lock in the best choice for the current step
        a[i] = best_choice
        
    print("YES")

# Read number of test cases
for _ in range(int(input())):
    solve()