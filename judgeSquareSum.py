class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r=0,int(math.sqrt(c))
        while l<=r:
            tot=l**2+r**2
            if tot==c:
                return True
            elif tot>c:
                r-=1
            else:
                l+=1
        return False