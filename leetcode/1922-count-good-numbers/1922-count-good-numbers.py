class Solution:
    def countGoodNumbers(self, n: int) -> int:
        oddpos=n//2
        evenpos=(n+1)//2
        MOD = 10**9 + 7
        def recurse(bas,countpos):

            if countpos==0:
                return 1
            half=recurse(bas,countpos//2)
            if countpos%2==0:
                return (half*half)%MOD
            else:
                return (half*half*bas)%MOD



        odd=recurse(4,oddpos)
        even=recurse(5,evenpos)

        return (odd*even)%MOD