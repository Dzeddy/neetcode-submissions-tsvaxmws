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
        next_level = collections.deque([])
        #current root
        curr = None
        res = []
        while curr or stack:
            curr_level = collections.deque([])
            while stack:
                curr = stack.popleft()
                if curr:
                    curr_level.append(curr.val)
                    next_level.append(curr.left)
                    next_level.append(curr.right)
            if curr_level:
                res.append(curr_level)
            else:
                break
            stack = next_level
            next_level = collections.deque([])
        return res
                        
