class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary(left,right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
            if left>right:
                return -1
            return binary(left,right)
        return binary(0,len(nums)-1)
        