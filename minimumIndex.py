from collections import Counter

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        
        dom = None
        for key, val in count.items():
            if val * 2 > n:
                dom = key
                break
        
        if dom is None: return -1
        
        current_dom_count = 0
        for index in range(n - 1):
            if nums[index] == dom:
                current_dom_count += 1
            
            left_len = index + 1
            right_len = n - left_len
            
            if current_dom_count * 2 > left_len and (count[dom] - current_dom_count) * 2 > right_len:
                return index
                
        return -1