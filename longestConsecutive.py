class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for key,val in count.items():
            if key-1 not in count:
                current=0
                item=key
                while item in count:
                    current+=1
                    item+=1
                ans=max(ans,current)
        return ans
