from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # player 0 = alice
        # player 1 = bob
        piles = tuple(piles)
        
        @lru_cache(maxsize=None)
        def dp(arr):
            if len(arr) == 1:
                # base case, we have a single array instance
                return arr[0]

            take_left = arr[0] - dp(arr[1:])

            take_right = arr[-1] - dp(arr[:len(arr) - 1])

            return max(take_left, take_right)

        return dp(piles) > 0

        # the above structure doesn't actually work because I want to return it two spaces up, which isn't rlly working
