class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
            
        max_k = -float('inf')
        
        stack = []
        
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            
            
            if curr < max_k:
                return True
                
           
            while stack and curr > stack[-1]:
                max_k = stack.pop()
                
            stack.append(curr)
            
        return False