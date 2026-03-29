class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        arr = [0] * len(nums)
        for i in range(len(nums)):
            arr[i] = max(arr[i-2] + nums[i], arr[i-1])
        print(arr)
        return arr[-1]