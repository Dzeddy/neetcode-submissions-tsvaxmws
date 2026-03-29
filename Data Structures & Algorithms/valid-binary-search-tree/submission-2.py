# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive solution: preorder traversal, check to see if 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        error = False
        def dfs(root):
            nonlocal error
            if not root:
                return
            dfs(root.left)
            if res:
                if root.val <= res[-1]:
                    error = True
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)

        return not error