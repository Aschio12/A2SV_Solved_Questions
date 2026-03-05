class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre={0:1}
        p,count=0,0
        for i in range(len(nums)):
            p+=nums[i]
            if p-k in pre:
                count+=pre[p-k]
            if p in pre:
                pre[p]+=1
            else:
                pre[p]=1
        return count

