# [1,2,-3,4]
# [1,2] -3 [4]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # our choice at every stage is to take and continue our array or skip and start a new array
        # thus, we have to set our max array and min array to: 
        n = len(nums)

        arr = [1] * n 
        narr = [1] * n

        arr[0] = nums[0]
        narr[0] = nums[0]

        msf = arr[0]

        for i in range(1, len(nums)):
            arr[i] = max(arr[i - 1] * nums[i], narr[i - 1] * nums[i], nums[i])
            narr[i] = min(arr[i - 1] * nums[i], narr[i - 1] * nums[i], nums[i])

            msf = max(arr[i], msf)
        
        return msf