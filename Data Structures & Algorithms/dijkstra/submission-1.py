class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dist = {}

        for i in range(n):
            dist[i] = sys.maxsize

        dist[src] = 0

        adjlist = defaultdict(list)

        for u, v, w in edges:
            adjlist[u].append((v,w))

        pq = [(0, src)]

        while pq:
            cost, curr = heapq.heappop(pq)

            if dist[curr] < cost:
                continue
            
            dist[curr] = cost

            for nei, cn in adjlist[curr]:
                nd = cost + cn

                if nd < dist[nei]:
                    heapq.heappush(pq, (nd, nei))

        for i in range(n):
            if dist[i] == sys.maxsize:
                dist[i] = -1

        return dist
