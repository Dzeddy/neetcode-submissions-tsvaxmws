# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        def dfs(root, max_so_far):
            nonlocal count
            if not root:
                return
            if root.val >= max_so_far:
                count += 1
            n_m = max(max_so_far, root.val)
            dfs(root.right, n_m)
            dfs(root.left, n_m)
        dfs(root, -101)

        return count