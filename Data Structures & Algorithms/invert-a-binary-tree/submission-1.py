# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr.left, curr.right = curr.right, curr.left
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right
        return root
            

        return root