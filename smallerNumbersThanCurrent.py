class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        c=Counter(nums)
        d=len(nums)

        for index,val in enumerate(nums):
            arr.append((val,index))

        arr.sort(reverse=True)
        hold={}
        
        for val,i in (arr):
            if val in hold:
                nums[i]=hold[val]
            else:
                nums[i]=d-c[val]
                hold[val]=d-c[val]
                d-=c[val]
                
        return nums


