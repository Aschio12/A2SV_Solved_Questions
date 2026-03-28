# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr=defaultdict(int)
        def rec(r,kk):
            if not r:
                return False
            if kk-r.val in arr:
                return True
            arr[r.val]+=1
            return rec(r.left,kk) or rec(r.right,kk)

        return rec(root,k)