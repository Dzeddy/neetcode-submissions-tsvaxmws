# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([root])
        res = []
        level = []
        while stack:
            s_l = len(stack)
            for i in range(s_l):
                curr = stack.popleft()
                if curr:
                    stack.append(curr.left)
                    stack.append(curr.right)
                    level.append(curr.val)
            if level:
                res.append(level)
            level = []
        return [i[-1] for i in res]