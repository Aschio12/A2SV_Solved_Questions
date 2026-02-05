class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first,last=strs[0],strs[-1]
        ans=""
        for i in range(min(len(first),len(last))):
            if first[i]==last[i]:
                ans+=first[i]
            else:
                break
        return ans



