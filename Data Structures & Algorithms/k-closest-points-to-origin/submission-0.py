class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eucld(x1,x2,y1,y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        eucldarr = [(eucld(0,i[0],0,i[1]),i) for i in points]

        heapq.heapify(eucldarr)

        res = []

        for i in range(k):
            res.append(heapq.heappop(eucldarr)[1])
        
        return res