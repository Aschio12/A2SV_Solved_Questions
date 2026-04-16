class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        #left and right piles are the minimum and the maximum therotical pile we can have
        left_pil,right_pil=1,sum(candies)//k
        
        if sum(candies)<k:
            return 0

        ans=0
        while left_pil<=right_pil:
            mid=(left_pil+right_pil)//2

            kid=0
            for pile in candies:
                kid+=pile//mid
            
            if kid>=k:
                ans=max(ans,mid)
                left_pil=mid+1
            elif kid<k:
                right_pil=mid-1
        return ans


        