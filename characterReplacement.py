class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m,ans,l,d=0,0,0,defaultdict(int)
        for r in range(len(s)):
            d[s[r]]+=1
            m=max(m,d[s[r]])
            if (r-l+1)-m>k:
                d[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans