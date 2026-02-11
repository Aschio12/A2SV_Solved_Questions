class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        ans=[""]*n
        for index,ch in zip(indices,s):
            ans[index]=ch
        return "".join(ans)

        