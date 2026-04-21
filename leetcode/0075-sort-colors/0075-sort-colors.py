class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count=[0,0,0]
        for n in nums:
            count[n]+=1
        i,k=0,0
        while i<len(nums):
            if count[k]>0:
                nums[i]=k
                count[k]-=1
                i+=1
            else:
                k+=1
            

        

        


                