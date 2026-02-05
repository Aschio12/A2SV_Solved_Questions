#User function Template for python3
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a.sort()
        b.sort()
        bi=0
        for i in range(len(a)):
            if bi<len(b) and b[bi]==a[i]:
                bi+=1
                
        return bi==len(b)
    
    
    
    
