"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        d=defaultdict(int)

        for emp in employees:
            d[emp.id]=emp
        
        def dfs(at):

            current_node=d[at]
            current_tot=current_node.importance
            for ids in current_node.subordinates:
                current_tot+=dfs(ids)
            return current_tot


        return dfs(id)