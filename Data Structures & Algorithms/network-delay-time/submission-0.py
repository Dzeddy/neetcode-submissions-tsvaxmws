class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's lmao

        dist = [float('inf') for _ in range(n)]

        dist[k - 1] = 0

        adjlist = defaultdict(list)

        for u, v, w in times:
            adjlist[u - 1].append((v - 1, w))

        pq = [(0, k - 1)]

        while pq:
            d, curr = heapq.heappop(pq)

            if d > dist[curr]:
                continue

            for nei, c in adjlist[curr]:
                nc = d + c
                if nc < dist[nei]:
                    dist[nei] = nc
                    heapq.heappush(pq, (nc, nei))
            
        maximillian = max(dist)

        return maximillian if maximillian < float('inf') else -1