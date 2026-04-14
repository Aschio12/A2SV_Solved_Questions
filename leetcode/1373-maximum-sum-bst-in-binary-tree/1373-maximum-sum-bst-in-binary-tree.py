# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ans=0
        
        def maxbst(root):
            nonlocal ans
            if not root:
                return [True,float("inf"),float("-inf"),0]
            
            is_left,mi_left,ma_left,tot_l=maxbst(root.left)
            is_right,mi_right,ma_right,tot_r=maxbst(root.right)
            if is_left and is_right and ma_left<root.val and mi_right>root.val:
                current=tot_l+root.val+tot_r
                ans=max(ans,current)
                mi_left=min(mi_left,root.val)
                ma_right=max(ma_right,root.val)
                return [True,mi_left,ma_right,current]
            else:
                return [False,0,0,0]
        
            
            
        
        maxbst(root)
        return ans
        