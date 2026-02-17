class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word11=Counter(word1)
        word22=Counter(word2)
        if len(word1)!=len(word2):
            return False
        for key in word11:
            if key not in word22:
                return False
        if sorted(word11.values())==sorted(word22.values()):
            return True

        else:
            return False
        
