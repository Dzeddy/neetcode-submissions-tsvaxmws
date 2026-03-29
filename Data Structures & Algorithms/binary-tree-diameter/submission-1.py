# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # idea: track the max value outside of the recursive loop. 
        # calculate the diameter at each root, through returning the height of the 
        # longest subtree of its children and adding them together + 1 for our current node
        
        # treat a None node as -1 ? or 0
        # calculate a node's diameter as the 
        max_diameter = 0

        def dfs(root):
            nonlocal max_diameter
            
            if not root:
                return -1
            left_subtree = dfs(root.left) + 1

            right_subtree = dfs(root.right) + 1

            max_diameter = max(max_diameter, left_subtree + right_subtree)

            return max(left_subtree, right_subtree)
        
        dfs(root)

        return max_diameter