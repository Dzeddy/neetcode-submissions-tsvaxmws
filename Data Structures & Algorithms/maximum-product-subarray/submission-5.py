# [1,2,-3,4]
# [1,2] -3 [4]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        narr = [1] * len(nums)
        arr[0] = nums[0]
        narr[0] = nums[0]
        maximillian = nums[0]
        for i in range(1, len(nums)):
            arr[i] = max(arr[i-1] * nums[i], nums[i], narr[i-1] * nums[i])

            narr[i] = min(narr[i-1] * nums[i], arr[i-1] * nums[i], nums[i])

            maximillian = max(arr[i], maximillian)
        print(arr)
        print(narr)
        return maximillian