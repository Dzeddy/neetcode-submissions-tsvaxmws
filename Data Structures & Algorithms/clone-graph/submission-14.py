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
        root_copy = Node(1)
        nodeMap = {1 : root_copy}
        q = deque([node])
        curr = None
        visited = set()
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            copy = nodeMap[curr.val]
            neighbors = curr.neighbors
            for i in neighbors:
                if i in visited:
                    continue
                if i.val not in nodeMap:
                    nodeMap[i.val] = Node(i.val)
                    q.append(i)
                copy.neighbors.append(nodeMap[i.val])
                nodeMap[i.val].neighbors.append(copy)

        return root_copy