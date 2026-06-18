class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # logic: if an island has 0 neighbors, it is 4
        # if an island has neighbors, then the side it has with the neighbors is removed from both of them

        # how can we implement this logic efficiently?

        # logic: only add to the perimeter if we reach a boundary (only add to the perimeter if you explore it and there's water)

        i_i, i_j = -1, -1

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        visited = set()

        count = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]:
                    i_i = i
                    i_j = j

        dq = collections.deque([(i_i, i_j)])

        while dq:
            c_i, c_j = dq.popleft()

            if (c_i, c_j) in visited:
                continue

            visited.add((c_i, c_j))

            for i in range(4):
                n_i, n_j = c_i + dx[i], c_j + dy[i]

                if (n_i, n_j) in visited:
                    continue

                if n_i < 0 or n_i >= len(grid):
                    count += 1
                    # print(c_i, c_j, ": 1")
                    continue

                if n_j < 0 or n_j >= len(grid[0]):
                    count += 1
                    # print(c_i, c_j, ": 1")
                    continue

                if not grid[n_i][n_j]:
                    count += 1
                    # print(c_i, c_j, ": 1")
                    continue

                dq.append((n_i, n_j))

            # print()

        return count