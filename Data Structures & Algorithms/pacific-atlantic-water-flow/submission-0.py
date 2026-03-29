class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific tuples
        pacific_tuples = set()
        atlantic_tuples = set()
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        def bfs_water_flow(i, j):
            sett = set()
            q = deque([(i, j)])
            visited = set()
            while q:
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add((curr[0], curr[1]))
                for k in range(4):
                    i_curr, j_curr = curr[0] + dx[k], curr[1] + dy[k]
                    if (i_curr, j_curr) in visited:
                        continue
                    # visited.add((i_curr, j_curr))
                    if i_curr < 0 or i_curr >= len(heights):
                        continue
                    if j_curr < 0 or j_curr >= len(heights[0]):
                        continue
                    if heights[i_curr][j_curr] >= heights[curr[0]][curr[1]]:
                        sett.add((i_curr, j_curr))
                        q.append((i_curr, j_curr))

            return sett


        for i in range(len(heights)):
            pacific_tuples.add((i, 0))
            pacific_tuples = pacific_tuples.union(bfs_water_flow(i, 0))

        for i in range(len(heights[0])):
            pacific_tuples.add((0, i))
            pacific_tuples = pacific_tuples.union(bfs_water_flow(0, i))

        for i in range(len(heights)):
            atlantic_tuples.add((i, len(heights[0]) - 1))
            atlantic_tuples = atlantic_tuples.union(bfs_water_flow(i, len(heights[0]) - 1))

        for i in range(len(heights[0])):
            atlantic_tuples.add((len(heights) - 1, i))
            atlantic_tuples = atlantic_tuples.union(bfs_water_flow(len(heights) - 1, i))

        return list( list(i) for i in pacific_tuples.intersection(atlantic_tuples))