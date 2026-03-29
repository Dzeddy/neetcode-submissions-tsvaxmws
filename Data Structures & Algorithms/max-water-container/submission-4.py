class Solution:
    def calc_area(self, l,r,lidx,ridx):
        return min(l,r) * (ridx-lidx)
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maximillian = self.calc_area(heights[0], heights[len(heights) - 1], 0, len(heights) - 1)
        curr = 0
        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            curr = self.calc_area(heights[l], heights[r], l, r)
            if curr > maximillian:
                maximillian = curr
            print(l, r)
        return maximillian

