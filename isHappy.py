class Solution:
    def isHappy(self, n: int) -> bool:
        seen={}
        while n!=1 and n not in seen:
            seen[n]=1
            n=sum(int(digit)**2 for digit in str(n))

        return n==1


        
        