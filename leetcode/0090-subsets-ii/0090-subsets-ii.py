class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans=[]

        def rec(current,idx):
    
            self.ans.append(current[:])  
            for i in range(idx,len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                current.append(nums[i])
                rec(current,i+1)
                current.pop()



        rec([],0)
        return self.ans
        