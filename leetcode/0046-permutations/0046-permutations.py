class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans,sol=[],[]
        def sub():
            if len(sol)==len(nums):
                ans.append(sol[:])
                return
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    sub()
                    sol.pop()

            

        sub()
        return ans