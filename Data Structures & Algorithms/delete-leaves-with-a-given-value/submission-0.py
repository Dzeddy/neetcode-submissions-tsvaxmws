# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return True
            
            # did we delete the nodes, or are they none?
            ldon = dfs(root.left)
            rdon = dfs(root.right)

            if ldon and rdon:
                root.left = None
                root.right = None

                if root.val == target:
                    return True
                
                return False
            
            if ldon:
                root.left = None
            
            if rdon:
                root.right = None

            return False

        head = TreeNode(None, left=root)

        dfs(head)

        return head.left