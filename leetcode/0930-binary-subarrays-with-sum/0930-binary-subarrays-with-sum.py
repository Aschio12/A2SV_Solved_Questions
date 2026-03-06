class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d=defaultdict(int)
        d[0]=1
        ans,p=0,0
        for num in nums:
            p+=num
            if p-goal in d:
                ans+=d[p-goal]
            d[p]+=1
        return ans