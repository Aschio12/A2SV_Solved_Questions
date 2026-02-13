class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        temp=[row[:] for row in matrix]
        indexer=len(matrix)-1
        for col in range(len(matrix[0])):
            for row in range(len(matrix)-1,-1,-1):
                matrix[col][indexer-row]=temp[row][col]
        
        