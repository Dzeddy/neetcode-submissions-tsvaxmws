from math import ceil

def calc_eat_time(arr, rate):
    var = 0
    for i in arr:
        var += ceil(i / rate)
    return var

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid = 0
        
        if h == len(piles):
            return high

        lowest_valid = int(10e20)

        while low <= high:
            mid = (low + high) // 2

            res = calc_eat_time(piles, mid)

            if res <= h:
                lowest_valid = min(lowest_valid, mid)
                high = mid - 1
            elif res > h:
                low = mid + 1
        
        return lowest_valid
        