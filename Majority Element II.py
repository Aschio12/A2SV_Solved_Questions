class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans,count=set(),defaultdict(int)
        for num in nums:
            count[num]+=1
            if count[num]>len(nums)/3:
                ans.add(num)
        return list(ans)