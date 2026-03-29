class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eval(k):
            res = 0
            for i in piles:
                res += math.ceil(i / k)
            return res

        # our condition is that eval <= h
        # we are searching for the leftmost value
        # we want to keep mid in consideration

        l = 1
        r = max(piles)

        while l < r:
            m = (r - l) // 2 + l
            res = eval(m)
            if res <= h: # our answer is in the answer space, we want to reduce our search space.
                r = m
            else: # our m is not in the answer space, thus we discard it
                l = m + 1
        
        return l
