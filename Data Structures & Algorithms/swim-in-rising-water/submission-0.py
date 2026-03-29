class Solution:
    # define state, meaning of dist, transition, relaxation, and when to prune
    # our state is just the i, j coordinates of the current square
    # dist is min time to reach the square at i j 
    # transition is the neighboring squares. whenever we pop from our minheap, we want to store the min time it takes 
    # to reach the current square. note: we are not pushing time + 1 to our minheap. we can however push max
    # (time it takes to reach our original node, current_height) to the heap for the node (cus obviously that is the first time it's unlocked)
    # (that is our relaxation formula for a new node, and it's fine because the only state where it's actually
    # possible to reach a node is if the previous nodes unlock before the current node)
    # we want to prune if the value pushed to the stack is > the dist stored
    # we don't need to add any dimensions to our dist
    # implementation details: for our priority queue we want to have our priority / min priority be 
    # just the time it takes to get to the node (that way we can greedily search for the next min time)
    # we want to prune if the pushed dist is > the stored dist
    def swimInWater(self, grid: List[List[int]]) -> int:
        dist = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dist[0][0] = grid[0][0]

        stack = [(grid[0][0],0,0)]

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        m = len(grid)
        n = len(grid[0])

        while stack:
            d, i, j = heapq.heappop(stack)

            if d > dist[i][j]:
                continue

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if ni < 0 or ni >= m:
                    continue
                
                if nj < 0 or nj >= n:
                    continue
                
                npc = max(grid[ni][nj], d)

                if npc < dist[ni][nj]:
                    dist[ni][nj] = npc
                    heapq.heappush(stack, (npc, ni, nj))
        
        return dist[-1][-1]


            