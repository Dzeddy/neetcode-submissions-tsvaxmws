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

        tina = deque([node])
        chi = {node: Node(node.val)}

        while tina: 
            mhc = tina.popleft()

            for zyns in mhc.neighbors:
                if zyns not in chi:
                    chi[zyns] = Node(zyns.val)
                    tina.append(zyns)
                chi[mhc].neighbors.append(chi[zyns])

        return chi[node]

            