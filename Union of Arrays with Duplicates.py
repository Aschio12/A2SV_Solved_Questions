class Solution:    
    def findUnion(self, a, b):
        # code here
        ans=set()
        aa,bb=0,0
        while aa<len(a) or bb<len(b):
            if aa<len(a):
                ans.add(a[aa])
            if bb<len(b):
                ans.add(b[bb])
            aa+=1
            bb+=1
            
        return ans
                