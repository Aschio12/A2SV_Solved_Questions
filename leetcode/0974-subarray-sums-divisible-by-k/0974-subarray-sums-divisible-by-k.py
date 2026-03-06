from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem=defaultdict(int)
        prefix,res,rem[0]=0,0,1
        for i in nums:
            prefix+=i
            if prefix%k in rem:
                res+=rem[prefix%k]
            rem[prefix%k]+=1
        return res

