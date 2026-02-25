class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for index,char in enumerate(s):
            d[char]=index
        left=0
        m=float("-inf")
        ans=[]
        for right in range(len(s)):
            m=max(m,d[s[right]])
            if right==m:
                ans.append(right-left+1)
                left=right+1
        return ans
        