class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[[0]*len(matrix) for i in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                transpose[c][r]=matrix[r][c]
        return transpose