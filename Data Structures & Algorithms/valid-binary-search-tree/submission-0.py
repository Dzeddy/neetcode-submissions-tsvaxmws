# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, val, smallest_bigger, largest_smaller, is_left):
            if root is None:
                return True
            if root.val >= smallest_bigger or root.val <= largest_smaller:
                return False
            if (root.val > val and is_left) or (root.val < val and not is_left):
                return False
            elif root.val == val:
                return False
            else:
                print(root.val)
                return dfs(root.left, root.val, min(smallest_bigger, root.val), largest_smaller, True) and dfs(root.right, root.val, smallest_bigger, max(largest_smaller, root.val), False)
        return dfs(root, -(10**32), (10**32), -(10**32), False)