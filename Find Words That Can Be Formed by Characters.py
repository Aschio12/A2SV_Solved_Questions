class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=Counter(chars)
        ans=0
        for ch in words:
            required=Counter(ch)
            for el in ch:
                if el not in c or required[el]>c[el]:
                    break
            else:
                ans+=len(ch) 
        return ans

                        