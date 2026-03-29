# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        memo = {}
        maximillian = 0
        def len_longest_path(root):
            if not root:
                return -1
            if root in memo:
                return memo[root]
            val = max(len_longest_path(root.left), len_longest_path(root.right)) + 1
            memo[root] = val
            return val
        def dfs(root):
            nonlocal maximillian

            if not root:
                return
            
            maximillian = max(maximillian, len_longest_path(root.right) + len_longest_path(root.left) + 2)

            dfs(root.left)
            dfs(root.right)

            return
        
        dfs(root)

        return maximillian
            