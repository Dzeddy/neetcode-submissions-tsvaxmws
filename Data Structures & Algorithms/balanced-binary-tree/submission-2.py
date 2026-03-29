# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # how to check balance: check height of each subtree, and return False if 
        # there exists a subtree with improper length
        
        unbalanced = False

        def dfs(node):
            nonlocal unbalanced
            if not node:
                return -1

            left_subtree = dfs(node.left) + 1
            right_subtree = dfs(node.right) + 1

            if abs(left_subtree - right_subtree) > 1:
                unbalanced = True

            return max(left_subtree, right_subtree)

        dfs(root)

        return not unbalanced