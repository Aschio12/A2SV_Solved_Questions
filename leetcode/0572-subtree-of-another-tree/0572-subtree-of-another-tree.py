# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(main,sub):
            if not sub and not main:
                return True
            if main and sub and sub.val==main.val:
                return isSame(main.left,sub.left) and isSame(main.right,sub.right)

            return False
    

        
        if not subRoot:
            return True
        if not root:
            return False
        if isSame(root,subRoot):
            return True

        return  self.isSubtree(root.left,subRoot) or  self.isSubtree(root.right,subRoot)


        