class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eval(k):
            res = 0
            for i in piles:
                res += math.ceil(i / k)
            return res

        l = 1
        r = max(piles)

        while l < r:
            curr = l + (r - l) // 2
            time = eval(curr)
            if time <= h:
                r = curr
            else:
                l = curr + 1
        
        return l
