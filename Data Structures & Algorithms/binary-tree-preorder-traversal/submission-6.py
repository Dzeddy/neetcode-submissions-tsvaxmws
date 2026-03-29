# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # let us consider how this algorithm works

        # first, we append our current value to the res
        # afterwards, we dfs the left value, and then dfs the right value
        # contextually, this causes us to go as left as possible, and then after we go right afterwards.
        # however, the time we actually choose to append our unit to the res is different
        # this is done when it is visited, compared to the inorder, which goes left -> middle -> right

        stack = []

        while root or stack:
            if not root:
                root = stack.pop()
            else:
                res.append(root.val)
                stack.append(root.right)
                root = root.left 

        # def dfs(root):
        #     if root == None:
        #         return
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        return res