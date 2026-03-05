class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store={0:-1}
        current=0
        for i in range(len(nums)):
            current+=nums[i]
            if current%k not in store:
                store[current%k]=i
            else:
                if ((i)-(store[current%k]+1))+1>=2:
                    return True
        return False