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

        while stack or root:
            while root:
                # store the root val
                res.append(root.val)

                #mimics the recursion using an iterative stack
                stack.append(root)

                #mimics the behavior of the recursive calls
                root = root.right
            
            # since while isn't running, it is an invariate that the root = None here
            root = stack.pop()

            # mimics the final call of the function, which dfs the right
            root = root.left
        
        return res[::-1]

        

        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     dfs(root.right)
        #     res.append(root.val)
        # dfs(root)

        return res