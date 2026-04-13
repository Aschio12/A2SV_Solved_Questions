class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posdiag=set()
        negdiag=set()

        ans=[]
        board=[["."]*n for i in range(n)]

        def backtrack(r):
            if r==n:
                valid=["".join(row) for row in board]
                ans.append(valid)
                return

            for c in range(n):
                if c in col or r-c in negdiag or r+c in posdiag:
                    continue
                board[r][c]="Q"
                col.add(c)
                negdiag.add(r-c)
                posdiag.add(r+c) 

                backtrack(r+1)
                board[r][c]="."
                col.remove(c)
                negdiag.remove(r-c)
                posdiag.remove(r+c)


        backtrack(0)
        return ans