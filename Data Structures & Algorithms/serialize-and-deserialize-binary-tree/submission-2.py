# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("#")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ":".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stack = data.split(":")

        count = 0

        def dfs():
            nonlocal count

            if count >= len(stack):
                return None

            if stack[count] == "#":
                count += 1
                return None

            # root will never exist. we are currently building it
            curr = TreeNode(stack[count])
            
            count += 1
            left = dfs()
            right = dfs()
            
            curr.left = left
            curr.right = right

            return curr
        
        res = dfs()

        return res