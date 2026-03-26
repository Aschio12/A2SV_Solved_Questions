# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.min=float("inf")
    
        def rec(root,depth):
            if not root:
                return
            if depth>=self.min:
                return

            if not root.left and not root.right:
                self.min=min(self.min,depth)
                return 

            rec(root.left,depth+1)
            rec(root.right,depth+1)

            



        rec(root,0)
        return self.min+1 if self.min!=float("inf") else 0
        