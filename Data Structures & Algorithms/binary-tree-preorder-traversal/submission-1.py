# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        stack = []
        curr = root
        
        while curr or stack:
            if curr:
                stack.append(curr)
                arr.append(curr.val)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return arr

        # arr = [] #recursive gooner solution
        # def dfs(root):
        #     if not root:
        #         return
        #     nonlocal arr
        #     arr.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return arr