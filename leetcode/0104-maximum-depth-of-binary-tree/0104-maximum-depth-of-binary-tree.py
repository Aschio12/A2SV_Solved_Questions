# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        def depth(root,h):
            if not root:
                return h
            h+=1
            left=depth(root.left,h)
            right=depth(root.right,h)

            return max(left,right)

        return depth(root,0)
        
        