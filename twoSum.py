class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        arr=[]
        for index,val in enumerate(nums):
            arr.append([val,index])
        arr.sort()
        while l<r:
            if arr[l][0]+arr[r][0]>target:
                r-=1
            elif arr[l][0]+arr[r][0]<target:
                l+=1
            else:
                return [arr[l][1],arr[r][1]]
        