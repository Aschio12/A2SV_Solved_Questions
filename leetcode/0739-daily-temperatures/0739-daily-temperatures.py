class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr=[[val,index] for index,val in enumerate(temperatures)]
        stack=[]
        ans=[0]*(len(arr))

        for val,index in arr:
            while stack and val>stack[-1][0]:
                ans[stack[-1][1]]=(index)-stack[-1][-1]
                stack.pop()
            if not stack or val<=stack[-1][0]:
                stack.append([val,index])
            
        return ans

