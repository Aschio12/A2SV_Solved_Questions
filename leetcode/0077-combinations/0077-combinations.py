class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[num for num in range(1,n+1)]
        ans=[]

        def rec(start,comb):
            if len(comb)==k:
                ans.append(comb[:])
                return

            

            for i in range(start,n+1):
                comb.append(i)
                rec(i+1,comb)
                comb.pop()


                 
        rec(1,[])
        return ans


        
        