class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col=set(),set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)
        for rr in list(row):
            for c in range(len(matrix[0])):
                matrix[rr][c]=0
        for cc in list(col):
            for r in range(len(matrix)):
                matrix[r][cc]=0