# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1, stack2 = [], []
        currp, currq = p, q

        if (p and not q) or (q and not p):
            return False

        while stack1 or currp:
            if currp:
                if not currq:
                    return False
                elif currp.val != currq.val:
                    return False
                stack1.append(currp)
                stack2.append(currq)
                currp = currp.left
                currq = currq.left
            else:
                if currq:
                    return False
                currp = stack1.pop()
                currq = stack2.pop()
                currp = currp.right
                currq = currq.right
        return not (currq or stack2)

