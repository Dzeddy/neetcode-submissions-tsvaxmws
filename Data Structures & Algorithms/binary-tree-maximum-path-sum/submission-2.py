# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # return max of max path left, max path right at each node, and return 0 if that + current node value is 0
        # also compute max at every point

        maxx = -10**6

        def dfs(node):
            nonlocal maxx

            if not node:
                return 0
            
            left_path = dfs(node.left)
            right_path = dfs(node.right)

            max_path = max(left_path, right_path) + node.val

            if max_path < 0: max_path = 0

            maxx = max(maxx, left_path + right_path + node.val)

            return max_path
        
        dfs(root)

        return maxx