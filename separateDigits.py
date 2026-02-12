class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            for s in str(num):
                ans.append(int(s))
        return ans 