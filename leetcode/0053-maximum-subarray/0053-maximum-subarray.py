class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')  # Initialize to the smallest possible number
        
        for num in nums:
            # Add the current number to the subarray sum or start a new subarray
            current_sum = max(num, current_sum + num)
            # Update the maximum sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum
