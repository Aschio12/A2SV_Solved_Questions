class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans=0
        for i in range(len(citations)):
            if citations[i]>=i+1:
                ans+=1
            else:
                break
        return ans