# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive solution: preorder traversal, check to see if 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        error = False
        def dfs(root):
            nonlocal error
            nonlocal prev
            if not root or error:
                return
            dfs(root.left)
            if prev is not None:
                if root.val <= prev:
                    error = True
                    return
            prev = root.val
            dfs(root.right)
        
        dfs(root)

        return not error