class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top,left,right,bottom=-1,-1,len(matrix[0]),len(matrix)

        ans=[]

        while left<=right and top<=bottom:
            #left-right:
            lp=left+1
            while lp<right:
                ans.append(matrix[top+1][lp])
                lp+=1
            
            lp-=1
            top+=1
            if top==bottom-1:
                break

            #top-bottom
            bp=top+1
            while bp<bottom:
                ans.append(matrix[bp][right-1])
                bp+=1
            bp-=1
            right-=1

            if right==left+1:
                break

            #right-left
            rl=right-1
            while rl>left:
                ans.append(matrix[bottom-1][rl])
                rl-=1

            rl+=1
            bottom-=1

            if bottom==top+1:
                break

            #bottom-top
            bt=bottom-1

            while bt>top:
                ans.append(matrix[bt][left+1])
                bt-=1

            bt+=1
            left+=1
            
            if left==right-1:
                break
        return ans



