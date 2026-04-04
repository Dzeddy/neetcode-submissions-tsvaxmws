class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []

        for l, r in intervals:
            if not res or l > res[-1][-1]:
                res.append([l,r])
            else:
                res[-1][-1] = max(res[-1][-1], r)
        
        return res