# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # recursive version
        # idea: first start going as left as possible
        # afterwards, if root is none, you return and then the most recent value in the stack gets put into res
        # following that, you dfs the right of said ancestor, and repeat the whold idea
        # mimicking this using a stack, we can write an iterative version

        stack = []
        prev = None

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and prev != peek.right:
                    root = peek.right
                else:
                    res.append(peek.val)
                    prev = stack.pop()

        return res
        

        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     dfs(root.right)
        #     res.append(root.val)
        # dfs(root)

        return res