class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        def swap(i):
            n=len(s)
            if i>=int(n//2):
                return
            s[i],s[n-(i+1)]=s[n-(i+1)],s[i]
            swap(i+1)
        swap(0)
        
        