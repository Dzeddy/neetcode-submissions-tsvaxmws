class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))

        def dfs(grid, r, c, temp):
            if min(r, c) < 0 or r == row or c == col or (r, c) in temp or grid[r][c] == 1:
                return 0
            if r == row - 1 and c == col - 1:
                return 1
            
            temp.add((r, c))
            
            count = 0

            for dy, dx in directions:
                count += dfs(grid, r + dx, c + dy, temp)
            
            temp.remove((r, c))

            return count
        return dfs(grid, 0, 0, set())

            