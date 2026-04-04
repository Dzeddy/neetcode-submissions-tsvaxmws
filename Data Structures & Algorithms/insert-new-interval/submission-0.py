class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        res = []

        for l, r in intervals:
            if not res or l > res[-1][-1]:
                res.append([l,r])
            else:
                res[-1][-1] = max(res[-1][-1],r)

        return res 