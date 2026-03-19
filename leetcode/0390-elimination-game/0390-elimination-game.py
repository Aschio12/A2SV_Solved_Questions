class Solution:
    def lastRemaining(self, n: int) -> int:
        head,left,remain=1,True,n
        step=1
        while remain>1:

            if left or remain%2==1:
                head+=step

            step*=2
            remain//=2

            left=not left

        return head

            
        