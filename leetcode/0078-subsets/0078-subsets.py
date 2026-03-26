class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def rec(proc,idx):
            ans.append(proc[:])
            if idx==len(nums):
                return
            
            for i in range(idx,len(nums)):
                proc.append(nums[i])
                rec(proc,i+1)
                proc.pop()
        rec([],0)
        return ans
