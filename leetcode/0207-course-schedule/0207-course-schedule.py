class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph=defaultdict(list)
        indegree=[0]* (numCourses)

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1

        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            current=q.popleft()
            ans.append(current)

            for fam in graph[current]:
                indegree[fam]-=1
                if indegree[fam]==0:
                    q.append(fam)
        return len(ans)==numCourses

            

        
            

