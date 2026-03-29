# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # it's a binary search tree, so we should search for a node where 
        # the split occurs nature of a binary search tree: left = smaller, right = larger
        # our lca will be >= p and < q 
        # not a bfs / dfs question, but more like a binary search question
        # we can do this with a while loop, but what is our exit condition?
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root 

        return root