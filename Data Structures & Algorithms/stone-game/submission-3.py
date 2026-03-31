from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # player 0 = alice
        # player 1 = bob
        piles = tuple(piles)

        @lru_cache(maxsize=None)
        def dp(l, r):
            if r - l == 0:
                # base case, we have a single array instance
                return piles[l]

            take_left = piles[l] - dp(l + 1, r)

            take_right = piles[r] - dp(l, r - 1)

            return max(take_left, take_right)

        res = dp(0, len(piles) - 1)
        
        print(res)

        return res > 0

        # the above structure doesn't actually work because I want to return it two spaces up, which isn't rlly working
