class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eval(k):
            res = 0
            for i in piles:
                res += math.ceil(i / k)
            return res
        
        min_val = max(piles)

        l = 1
        r = max(piles)

        while l < r:
            curr = l + (r - l) // 2
            time = eval(curr)
            if time <= h:
                min_val = min(min_val, curr)
                r = curr
            else:
                l = curr + 1
        
        return min_val
