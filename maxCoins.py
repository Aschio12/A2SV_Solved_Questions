class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        mine=0
        piles.sort(reverse=True)
        cycle=len(piles)//3
        for i in range(1,len(piles),2):
            if cycle==0:
                break
            mine+=piles[i]
            cycle-=1
        return mine
        