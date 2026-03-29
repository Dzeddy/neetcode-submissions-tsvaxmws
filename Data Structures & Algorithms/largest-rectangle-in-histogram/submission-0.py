class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # what if we group them by multiples?
        # not worth, because 1. 
        # n^2 solution is obvious. pick point 1, iterate down array in both directions and go until we are stopped
        # what if we store all the heights so far and their prev indices and then wipe it if we hit a 0?
        # that's still a n^2 bound because if the array has different lengths @ every point
        # what if we store max so far and min so far? not useful either
        mono = []

        maximillian = 0

        for idx, i in enumerate(heights):
            last_idx = idx
            while mono:
                cidx, curr = mono[-1]
                if i < curr:
                    mono.pop()
                    maximillian = max(maximillian, (idx - cidx) * curr)
                    last_idx = cidx
                else:
                    if i == curr:
                        last_idx = cidx
                    break

            if not mono or mono[-1][1] != i:
                mono.append((last_idx, i))

        while mono:
            nidx, ni = mono.pop()
            maximillian = max(maximillian, (len(heights) - nidx) * ni)

        return maximillian