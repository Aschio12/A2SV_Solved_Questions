# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def even(root,parent,grand):
            if not root:
                return 0

            ans=0

            if grand!=None and grand.val%2==0:
                ans+=root.val
            ans+=even(root.left,root,parent)
            ans+=even(root.right,root,parent)

            return ans
        return even(root,None,None)
            
            
            
            

        
