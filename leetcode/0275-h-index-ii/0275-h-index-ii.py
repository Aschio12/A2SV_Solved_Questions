class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right,n=0,len(citations)-1,len(citations)
        while left<=right:
            mid=(left+right)//2
            if citations[mid]<n-mid:
                left=mid+1
            elif citations[mid]>n-mid:
                right=mid-1
            else:
                return n-mid
        return n-left

