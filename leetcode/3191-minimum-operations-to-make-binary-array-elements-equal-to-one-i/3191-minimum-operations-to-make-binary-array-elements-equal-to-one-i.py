class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n,count=len(nums),0
        for i in range(n-2):
            if nums[i]==0:
                nums[i]=1
                if nums[i+1]==0:
                    nums[i+1]=1
                else:
                    nums[i+1]=0
                if nums[i+2]==0:
                    nums[i+2]=1
                else:
                    nums[i+2]=0
                count+=1
        return -1 if nums[n-1]==0 or nums[n-2]==0 else count
