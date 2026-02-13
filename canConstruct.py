class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran=defaultdict(int)
        mag=defaultdict(int)
        for el in ransomNote:
            ran[el]+=1
        for el in  magazine:
            mag[el]+=1
        
        for key,val in ran.items():
            if key not in mag or mag[key]<val:
                return False
        return True