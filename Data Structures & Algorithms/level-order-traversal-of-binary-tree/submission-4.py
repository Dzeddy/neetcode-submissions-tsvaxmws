# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = collections.deque([root])
        res = []
        level = []
        curr = root
        while stack:
            s_l = len(stack)
            for i in range(s_l):
                curr = stack.popleft()
                if curr:
                    level.append(curr.val)
                    stack.append(curr.left)
                    stack.append(curr.right)
            if level:
                res.append(level)
                level = []
        return res