# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive solution: preorder traversal, check to see if sorted
    # inefficient space wise
    # we can track the largest value that our node should be greater than, and the smallest value our node should be less than
    # note: left should mean our node is smaller than the current node, right should mean our node is greater than the current node
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = False
        def dfs(root, slt, lgt):
            nonlocal flag
            #let's consider the logic: smallest value that our root should be less than, if we move left, should be our root
            # largest value that our root should be greater than, if we move right, should again be our root
            if not root:
                return
            if root.val >= slt:
                flag = True
            if root.val <= lgt:
                flag = True
            dfs(root.left, root.val, lgt)
            dfs(root.right, slt, root.val)
        dfs(root, 1001, -1001)
        return not flag
            
