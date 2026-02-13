class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        up=True
        row,col=0,0
        ans=[]
        condtion=True
        while len(ans)<len(matrix)*len(matrix[0]):
            if up:
                while row>=0 and col<len(matrix[0]):
                    ans.append(matrix[row][col])
                    row-=1
                    col+=1
                up=not up
                if col==len(matrix[0]):
                    col-=1
                    row+=2
                else:
                    row+=1
                     
            else:
                while row<len(matrix) and col>=0:
                    ans.append(matrix[row][col])
                    row+=1
                    col-=1
                up=not up
                if row==len(matrix):
                   col+=2
                   row-=1
                else:
                    col+=1
           
        return ans