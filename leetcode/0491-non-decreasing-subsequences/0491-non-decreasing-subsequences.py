class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        def rec(current,idx):
            if len(current)>=2:
                self.ans.append(current[:])
            used=set()
            for i in range(idx,len(nums)):
                if nums[i] in used:
                    continue
                if not current or nums[i]>=current[-1]:
                    used.add(nums[i])
                    current.append(nums[i])
                    rec(current,i+1)
                    current.pop()


        rec([],0)
        
        return self.ans


        
