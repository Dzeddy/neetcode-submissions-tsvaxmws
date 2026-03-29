# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #tracks current level
        stack = collections.deque([root])
        #current root
        curr = None
        res = []
        while curr or stack:
            curr_level = []
            z = len(stack)
            for i in range(z):
                curr = stack.popleft()
                if curr:
                    curr_level.append(curr.val)
                    stack.append(curr.left)
                    stack.append(curr.right)
            if curr_level:
                res.append(curr_level)
            next_level = collections.deque([])
        return res
                        
