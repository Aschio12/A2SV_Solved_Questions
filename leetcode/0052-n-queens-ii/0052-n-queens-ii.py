class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=0
        board=[["."]*n for i in range(n)]
        cols=set()
        posdiag=set()
        negdiag=set()

        def backtrack(r):
            nonlocal ans
            if r==n:
                ans+=1
                return

            for c in range(n):
                if c in cols or r-c in negdiag or r+c in posdiag:
                    continue

                board[r][c]="Q"
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                backtrack(r+1)
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)

        backtrack(0)
        return ans

