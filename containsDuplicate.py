class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt={}
        for i in (nums):
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        dictt=list(dictt.values())
        for i in dictt:
            if i>=2:
                return(True)
        return(False)
            
    