class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # brute force solution: enumerate all subarrays, check if turbulent
        # n^3
        # bad
        
        # clearly sliding window has potential here
        # just convert it into increasing or decreasing

        # 2 (can be taken regardless) 4 3 2 2 5 1 4
        # 2 1 0 0 0 1 0 1
        # what to do with the 2? 
        # set it to the opposite of the thing in front of it
        # problem is arr length can = 1. In this case, we should just return 1 to avoid out of bounds

        if len(arr) == 1:
            return 1

        narr = [0] * (len(arr) - 1)

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                narr[i - 1] = 1
            elif arr[i] < arr[i - 1]:
                narr[i - 1] = 0
            else:
                narr[i - 1] = -1

        # sliding window

        l = 0
        r = 0

        last = None

        maxx = 1

        while r < len(narr):
            # when do we want to move r + = 1? 
            # if last = 0, when r = 1
            # if last = 1, when r = 0
            # when do we want to move left forward?
            # if r = -1 or if r = last

            if narr[r] == last or narr[r] == -1:
                l = r + 1 if narr[r] == -1 else r
                last = narr[r]
                r += 1
                continue
            
            maxx = max(r - l + 2, maxx)
            last = narr[r]
            r += 1

        return maxx