class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()
        def dfs(current):

            if current==destination:
                return True
            if current in visited:
                return False

            visited.add(current)

            for node in graph[current]:
                if dfs(node)==True:
                    return True
            return False
        return dfs(source)
