class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pp=Counter(pattern)
        so=s.split()
        mapping={}
        seen=set()
        if len(pattern)!=len(so):
            return False
        for index,ch in enumerate(pattern):
            if ch in mapping:
                if mapping[ch]!=so[index]:
                    return False
            else:
                if so[index] in seen:
                    return False
                mapping[ch]=so[index]
                seen.add(so[index])

        return True 