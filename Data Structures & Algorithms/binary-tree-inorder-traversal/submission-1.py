# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        arr = []

        while (curr or stack):
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                arr.append(curr.val)
                curr = curr.right
        return arr


        # def dfs(root):
        #     if not root:
        #         return
        #     nonlocal arr
        #     dfs(root.left)
        #     arr.append(root.val)
        #     dfs(root.right)
        #     return
        # dfs(root)
        # return arr

        
            