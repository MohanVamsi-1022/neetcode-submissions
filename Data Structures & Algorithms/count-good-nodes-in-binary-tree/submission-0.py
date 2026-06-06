# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node,max_num):
            nonlocal res
            if not node:
                return
            if node.val >= max_num:
                res += 1
            max_num = max(max_num,node.val)
            dfs(node.left,max_num)
            dfs(node.right,max_num)
        dfs(root,float("-inf"))
        return res

        
        