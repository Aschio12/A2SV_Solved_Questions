class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])

        c,cost=0,0

        for a,b in costs:
            
            if c<len(costs)//2:
                cost+=a
            else:
                cost+=b
            c+=1
        return cost