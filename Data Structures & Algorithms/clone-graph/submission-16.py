"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stack = deque([node])
        mapp = {node : Node(node.val)}
        visited = set([node])

        while stack:
            curr = stack.popleft()
            for i in curr.neighbors:
                if i not in mapp:
                    mapp[i] = Node(i.val)
                    stack.append(i)
                mapp[curr].neighbors.append(mapp[i])
                    
        return mapp[node] if node in mapp else None
            