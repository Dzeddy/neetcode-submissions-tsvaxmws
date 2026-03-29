class Solution:
    # i should have just popped by num cost
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra's, but check both current cost and number of stops
        # at each step, increment number of stops
        # kill if number of stops > k

        adjlist = defaultdict(list)

        costs = [float('inf') for _ in range(n)]

        costs[src] = 0

        # build adjacency list
        for u, v, w in flights:
            adjlist[u].append((v, w))

        pq = [(0,src,0)]

        while pq:
            nf, curr, d = heapq.heappop(pq)
            
            if nf == k + 1: # we can't explore any more
                continue

            for nei, c in adjlist[curr]:
                nd = d + c
                nnf = nf + 1
                # we want two scenarios, 1 where we consider that nd is the destination. in this case, we are fine 
                # if nd != destination, if we are out of flights we can't actually call that a new cost
                if nd < costs[nei]:
                    costs[nei] = nd
                    heapq.heappush(pq, (nnf, nei, nd))

        return costs[dst] if costs[dst] < float('inf') else -1


