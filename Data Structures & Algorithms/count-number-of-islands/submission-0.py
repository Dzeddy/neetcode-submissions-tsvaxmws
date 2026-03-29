class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set([])
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                if grid[i][j] == "1":
                    count += 1
                    stack = [(i, j)]
                    local_visited = set([])
                    while stack:
                        curr = stack.pop()
                        for k in range(len(dx)):
                            temp = (curr[0] + dy[k], curr[1] + dx[k])
                            if temp[0] < 0 or temp[0] >= len(grid) or temp[1] < 0 or temp[1] >= len(grid[0]):
                                continue
                            if temp not in local_visited and grid[temp[0]][temp[1]] == "1":
                                local_visited.add(temp)
                                visited.add(temp)
                                stack.append(temp)
        return count