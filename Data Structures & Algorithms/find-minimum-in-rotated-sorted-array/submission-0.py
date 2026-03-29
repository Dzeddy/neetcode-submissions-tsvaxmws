class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        # cases: nums[l] > nums[r]
        # if m > nums[l], this means we need to search in the r side
        # elif m < nums[l], this means we need to search in the left side
        # nums[l] < nums[r]
        # our array is perfectly in order. return nums[l]


        while l < r:
            m = (r - l) // 2 + l
            
            left = nums[l]
            mid = nums[m]
            right = nums[r]

            if left > right:
                if mid >= left:
                    l = m + 1
                else:
                    r = m
            if left < right:
                return left
        
        return nums[l]
