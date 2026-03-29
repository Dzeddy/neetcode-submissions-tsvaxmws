class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        adjlist = defaultdict(list)
        
        for u, v in edges:
            adjlist[u].append(v)
            indegree[v] += 1
        
        stack = []

        for i in range(n):
            if indegree[i] == 0:
                stack.append(i)
        
        res = []

        while stack:
            curr = stack.pop()
            res.append(curr)
            for nei in adjlist[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    stack.append(nei)

        return res if len(res) == n else []