# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        arr = []
        stack = []
        visited = set()
        while curr or stack:
            if curr:
                arr.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                curr = None
            else:
                curr = stack.pop()
        return arr[::-1]
        # arr = [] # gooning recursive solution
        # def dfs(root):
        #     if not root:
        #         return
        #     nonlocal arr
        #     dfs(root.left)
        #     dfs(root.right)
        #     arr.append(root.val)
        # dfs(root)
        # return arr
