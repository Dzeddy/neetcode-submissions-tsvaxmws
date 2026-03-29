class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_arr = (min(heights[l], heights[r]) * (r - l))
        while l < r:
            max_arr = max(max_arr, (min(heights[l], heights[r]) * (r - l)))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1 
            else:
                l += 1
                r -= 1
        return max_arr
        