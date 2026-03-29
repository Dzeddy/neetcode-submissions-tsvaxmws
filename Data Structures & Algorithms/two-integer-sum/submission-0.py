class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}

        for i in range(len(nums)):
            if nums[i] in dick:
                return [dick[nums[i]], i]
            dick[target - nums[i]] = i
        
        return -1
