class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans=[]
        current=""
        blocked=False
        for char in source:
            i=0
            while i<len(char):
                if not blocked:
                    if i+1<len(char) and char[i:i+2]=="//":
                        break
                    if i+1<len(char) and char[i]+char[i+1]=="/*":
                        blocked=True
                        i+=1
                    else:
                        current+=char[i]
                        
                else:
                    if i+1<len(char) and char[i]+char[i+1]=="*/":
                        blocked=False
                        i+=1
                i+=1
                  
            if current and not blocked:
                ans.append(current)
                current=""
        return ans
        