# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]

        while stack:
            c_p , c_q = stack.pop()

            if not c_p and not c_q:
                continue

            if c_p and not c_q:
                return False
            
            if c_q and not c_p:
                return False

            if c_p.val != c_q.val:
                return False
            
            stack.append((c_p.left, c_q.left))
            stack.append((c_p.right, c_q.right))
        
        return True