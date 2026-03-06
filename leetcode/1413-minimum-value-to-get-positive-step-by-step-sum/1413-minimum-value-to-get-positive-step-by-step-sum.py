class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_p=0
        prefix=0
        for i in nums:
            prefix+=i
            min_p=min(min_p,prefix)
        return max(1,1-min_p)