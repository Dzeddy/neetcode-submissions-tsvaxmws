class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        order = []
        visited = [False] * numCourses
        q = deque()
        indegree = [0] * numCourses
        for i in prerequisites:
            adjList[i[1]].append(i[0])
            indegree[i[0]] += 1
        for idx, i in enumerate(indegree):
            if i == 0:
                q.append(idx)
                order.append(idx)
        while q:
            curr = q.pop()
            if visited[curr]:
                continue
            visited[curr] = True
            for i in adjList[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                    order.append(i)
        print(order)
        if max(indegree) != 0:
            return []
        return order