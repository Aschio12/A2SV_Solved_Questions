# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:

        def dfs(root,current):
            if not root:
                return 
            current+=root.val
            if current-target in prefix:
                self.count+=prefix[current-target]
            
            if current in prefix:
                prefix[current]+=1
            else:
                prefix[current]=1

            dfs(root.left,current)
            dfs(root.right,current)
            prefix[current]-=1

            

        self.count=0
        prefix={0:1}
        dfs(root,0)
        return self.count
        