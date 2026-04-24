class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        original=image[sr][sc]
        if original==color:
            return image

        def dfs(sr,sc,original):
            if sc<0 or sc>len(image[0])-1 or sr<0 or sr>len(image)-1:
                return
            if image[sr][sc]==original:
                image[sr][sc]=color
            else:
                return
            dfs(sr-1,sc,original)
            dfs(sr,sc-1,original)
            dfs(sr,sc+1,original)
            dfs(sr+1,sc,original)

        dfs(sr,sc,original)
        return image