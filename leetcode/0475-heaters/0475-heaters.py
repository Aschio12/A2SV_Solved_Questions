class Solution:
    def findRadius(self, houses: List[int], heater: List[int]) -> int:
        heater.sort()
        n=len(heater)
        ans=float("-inf")

        for num in houses:
            idx1=bisect_left(heater,num)
            if idx1==0:
                current1=heater[0]-num
            elif idx1==n:
                current1=num-heater[n-1]
            else:
                current1=min(num-heater[idx1-1],heater[idx1]-num)
            ans=max(ans,current1)

        return ans
            

