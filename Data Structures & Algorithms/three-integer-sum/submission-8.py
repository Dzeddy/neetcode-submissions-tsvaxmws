class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        arr = []
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
        while target < len(nums) - 3:
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -nums[target]:
                    left += 1
                elif nums[left] + nums[right] > -nums[target]:
                    right -= 1
                else:
                    if sorted([nums[left], nums[right], nums[target]]) not in arr and len(set([left,right,target])) == 3:
                        arr.append(sorted([nums[left], nums[right], nums[target]]))
                    left += 1
            target += 1
        return arr