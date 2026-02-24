class Solution:
    def maxArea(self, height: List[int]) -> int:

        area,l,r=0,0,len(height)-1

        while l<r:
            current_area=min(height[l],height[r])*(r-l)
            area=max(current_area,area)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return area