class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        n=len(changed)
        if n%2!=0:
            return []

        count=Counter(changed)
        res=[]
        for i in range(n):
            if count[changed[i]]==0:
                continue
            count[changed[i]]-=1
            if count[changed[i]*2]>0:
                res.append(changed[i])
                count[changed[i]*2]-=1
            else:
                return []
        return res 
            
           
            
            

