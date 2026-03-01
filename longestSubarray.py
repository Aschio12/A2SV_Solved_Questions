class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        d={0:0,1:0}
        ans,l=0,0
        for r,c in enumerate(nums):
            d[c]+=1
            while d[0]>1 and l<r:
                d[nums[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans-1