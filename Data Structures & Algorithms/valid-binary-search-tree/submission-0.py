# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(low,node,high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (helper(low,node.left,node.val) and
            helper(node.val,node.right,high))
        return helper(float("-inf"),root,float("inf"))
        