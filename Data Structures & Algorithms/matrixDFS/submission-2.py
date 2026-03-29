class Solution:
    def countPaths(self, grid):
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        # Check if start or end is a rock
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return 0
        
        # Stack for DFS: (row, col, visited_set)
        stack = [(0, 0, {(0, 0)})]
        path_count = 0
        
        # Possible moves: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while stack:
            row, col, visited = stack.pop()
            
            # If reached the destination
            if row == rows - 1 and col == cols - 1:
                path_count += 1
                continue
            
            # Try all four directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is valid
                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    grid[new_row][new_col] == 0 and 
                    (new_row, new_col) not in visited):
                    
                    # Create a new visited set (to avoid modifying the current path's visited set)
                    new_visited = visited.copy()
                    new_visited.add((new_row, new_col))
                    
                    stack.append((new_row, new_col, new_visited))
        
        return path_count

            