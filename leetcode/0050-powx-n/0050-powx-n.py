class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
           
        def power(b,p):
            if p==0:
                return 1
            current=power(b,p//2)
            if p%2==0:
                return current*current
            else:
                return current*current*b


        return power(x,n)