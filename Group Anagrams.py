class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for index,char in enumerate(strs):
            current="".join(sorted(char))
            if current not in d:
                d[current]=[index]
            else:
                d[current].append(index)

                
        ans=[]
        for key,val in d.items():
            current=[]
            for v in val:
                current.append(strs[v])
            if current:
                ans.append(current)
        return ans