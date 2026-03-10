class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        temp=[row[:] for row in img]
        for row in range(len(img)):
            for col in range(len(img[0])):
                tot,count=0,0
                for i in range(row-1,row+2):
                    for j in range(col-1,col+2):
                        if i<0 or i==len(img) or j<0 or j==len(img[0]):
                            continue
                        tot+=temp[i][j]
                        count+=1
                img[row][col]=tot//count
        return(img)