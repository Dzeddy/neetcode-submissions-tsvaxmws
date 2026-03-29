# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # recursive version
        # idea: first start going as left as possible
        # afterwards, if root is none, you return and then the most recent value in the stack gets put into res
        # following that, you dfs the right of said ancestor, and repeat the whold idea
        # mimicking this using a stack, we can write an iterative version

        stack = []

        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
                
        return res