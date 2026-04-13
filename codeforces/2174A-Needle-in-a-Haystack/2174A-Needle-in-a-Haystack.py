import sys
from collections import Counter

def solve():
    # Fast I/O is critical for N = 200,000
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    try:
        t_cases = int(next(it))
    except StopIteration:
        return

    results = []
    
    for _ in range(t_cases):
        s = next(it)
        t = next(it)
        
        n_s = len(s)
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        
        # 1. Validation: Check if t has enough characters to form s
        possible = True
        for char, count in cnt_s.items():
            if cnt_t.get(char, 0) < count:
                possible = False
                break
        
        if not possible:
            results.append("Impossible")
            continue
            
        # 2. Identify the "Pool" (Characters in t not strictly needed for s)
        pool = []
        for char, total in cnt_t.items():
            extra = total - cnt_s.get(char, 0)
            if extra > 0:
                pool.extend([char] * extra)
        pool.sort()
        
        # 3. Lookahead Precomputation
        # Find the index of the next character in s that is different from s[i]
        next_diff = [n_s] * n_s
        for i in range(n_s - 2, -1, -1):
            if s[i] == s[i+1]:
                next_diff[i] = next_diff[i+1]
            else:
                next_diff[i] = i + 1
        
        # 4. Greedy Construction
        res = []
        s_idx = 0
        p_idx = 0
        n_pool = len(pool)
        
        while s_idx < n_s and p_idx < n_pool:
            char_s = s[s_idx]
            char_p = pool[p_idx]
            
            if char_p < char_s:
                # Pool character is smaller, use it to improve lexicographical rank
                res.append(char_p)
                p_idx += 1
            elif char_p > char_s:
                # s character is smaller, we must use it to maintain subsequence order
                res.append(char_s)
                s_idx += 1
            else:
                # Tie-break: if char_p == char_s
                # Check the first different character in s
                diff_pos = next_diff[s_idx]
                if diff_pos < n_s and s[diff_pos] < char_s:
                    # Defer the pool character to get to the smaller s character faster
                    res.append(char_s)
                    s_idx += 1
                else:
                    # No benefit to waiting, use the pool character now
                    res.append(char_p)
                    p_idx += 1
        
        # Append remaining characters
        res.extend(list(s[s_idx:]))
        res.extend(pool[p_idx:])
        
        results.append("".join(res))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()