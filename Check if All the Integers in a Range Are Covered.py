class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        prefix=[0]*52
        m=float("-inf")
        for l,r in ranges:
            prefix[l]+=1
            prefix[r+1]-=1
        p=0
        for i in range(1,right+1):
            p+=prefix[i]
            prefix[i]=p
            
        for i in range(left,right+1):
            if prefix[i]<=0:
                return False
            
        return True