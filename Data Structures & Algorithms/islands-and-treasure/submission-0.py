class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        deey = [0,1,0,-1]
        deex = [-1,0,1,0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    kek = (i, j)
                    visited.add(kek)
                    stack = [kek]
                    while stack:
                        new_i, new_j = stack.pop()

                        val = grid[new_i][new_j]

                        for k in range(4):
                            i_curr, j_curr = (new_i + deey[k], new_j + deex[k])
                            
                            if (i_curr == m or i_curr < 0) or (j_curr == n or j_curr < 0):
                                continue
                            elif grid[i_curr][j_curr] == -1:
                                continue
                            elif grid[i_curr][j_curr] == 2147483647:
                                grid[i_curr][j_curr] = val + 1
                                stack.append((i_curr, j_curr))
                            else:
                                if val + 1 < grid[i_curr][j_curr]:
                                    grid[i_curr][j_curr] = val + 1
                                    stack.append((i_curr, j_curr))
        return

                        

                        