class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edges_count=len(edges)
        d=defaultdict(int)
        for pair in edges:
            d[pair[0]]+=1
            d[pair[1]]+=1
            if d[pair[0]]==edges_count:
                return pair[0]
           
            if d[pair[1]]==edges_count:
                return pair[1]
            