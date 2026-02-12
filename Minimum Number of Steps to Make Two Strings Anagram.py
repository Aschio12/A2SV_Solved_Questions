class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tt=Counter(t)
        cc=Counter(s)
        ans=0
        for key,val in cc.items():
            if key  in tt:
                if val>tt[key]:
                    ans+=val-tt[key]
            else:
                ans+=val
        return ans
