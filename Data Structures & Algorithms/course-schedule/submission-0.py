class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = [False] * numCourses
        q = deque()
        indegree = [0] * numCourses
        for i in prerequisites:
            adjList[i[0]].append(i[1])
            indegree[i[1]] += 1
        for idx, i in enumerate(indegree):
            if i == 0:
                q.append(idx)
        while q:
            curr = q.pop()
            if visited[curr]:
                continue
            visited[curr] = True
            for i in adjList[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        print(indegree)
        if max(indegree) != 0:
            return False
        return True
            

            
