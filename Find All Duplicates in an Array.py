class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            index,val=abs(num)-1,abs(num)
            if nums[index]<0:
                ans.append(val)
            else:
                nums[index]*=-1
        return ans