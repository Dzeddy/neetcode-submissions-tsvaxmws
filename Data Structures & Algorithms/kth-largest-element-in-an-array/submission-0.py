class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neganums = [-i for i in nums]

        heapq.heapify(neganums)

        for i in range(k - 1):
            heapq.heappop(neganums)

        return -heapq.heappop(neganums)