class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        current=target
        ans=0
        while current>1:
            if maxDoubles==0:
                ans+=(current-1)
                break
            if current%2==0:
                current//=2
                ans+=1
                maxDoubles-=1
            else:
                current-=1
                ans+=1
        return ans

        