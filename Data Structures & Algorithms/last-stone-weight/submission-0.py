class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we can use negative numbers for a maxheap
        negastones = [-i for i in stones]
        heapq.heapify(negastones)

        while len(negastones) > 1:
            stone1 = heapq.heappop(negastones)
            stone2 = heapq.heappop(negastones)

            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                heapq.heappush(negastones, stone1 - stone2)
            elif stone1 > stone2:
                heapq.heappush(negastones, stone2 - stone1)
        
        return -negastones[-1] if negastones else 0