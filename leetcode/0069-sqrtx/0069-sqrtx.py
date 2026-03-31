class Solution:
    def mySqrt(self,target: int) -> int:
        self.ans=-1
        def binary(left,right):
            if left>right:
                return 

            mid=(left+right)//2
            
            if mid*mid>target:
                binary(left,mid-1)  
            else:
                self.ans=mid
                return binary(mid+1,right)
            
           

            
        
        binary(0,target)
        return self.ans
        