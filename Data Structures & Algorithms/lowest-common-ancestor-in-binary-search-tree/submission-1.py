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
        deepest = None
        def dfs(root, target, res):
            res.append(root)
            if root == target:
                return
            if root.val < target.val:
                dfs(root.right, target, res)
            elif root.val > target.val:
                dfs(root.left, target, res)
        
        res1 = []
        res2 = []
        dfs(root, p, res1)
        dfs(root, q, res2)

        print([i.val for i in res1])
        print([i.val for i in res2])

        for i in range(min(len(res1), len(res2))):
            if res1[i] != res2[i]:
                return res1[i-1]

        return res1[-1] if len(res1) < len(res2) else res2[-1]