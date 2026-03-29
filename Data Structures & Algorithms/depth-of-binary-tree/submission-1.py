# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dick = {root: 1}
        stack = []
        curr = root

        if not root:
            return 0
            
        while stack or curr:
            if curr:
                if curr.left:
                    stack.append(curr.left)
                    dick[curr.left] = dick[curr] + 1
                if curr.right:
                    stack.append(curr.right)
                    dick[curr.right] = dick[curr] + 1
                curr = None
            else:
                curr = stack.pop()
        return max(dick.values())
            
        # def dfs(root):
        #     if not root:
        #         return 0
        #     else:
        #         return max(dfs(root.left), dfs(root.right)) + 1
        # return dfs(root)