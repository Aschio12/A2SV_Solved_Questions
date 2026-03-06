class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ss=list(s)
        prefix_d=[0]*(len(s)+1)
        for l,r,d in shifts:
            prefix_d[r+1]+=1 if d else -1
            prefix_d[l]+=-1 if d else 1
            
        diff=0
        ans=[ord(c)-ord("a") for c in ss]
        for i in range(len(prefix_d)-1,-1,-1):
            diff+=prefix_d[i]
            ans[i-1]=(ans[i-1]+diff)%26
        answer=[chr(d+ord("a")) for d in ans]

        
        return "".join(answer)