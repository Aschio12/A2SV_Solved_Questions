class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans,l,sub=0,0,SortedList()
        for r  in range(len(nums)):
            sub.add(nums[r])
            while sub[-1]-sub[0]>limit:
                sub.remove(nums[l])
                l+=1
            ans=max(ans,r-l+1)
        return ans
           