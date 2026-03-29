class Solution:
    def search(self, nums: List[int], target: int) -> int:
        big = 0
        chungus = len(nums) - 1
        kms = (big + chungus) // 2

        while big <= chungus:
            kms = (big + chungus) // 2

            if nums[kms] == target:
                return kms
            elif nums[kms] < target:
                big = kms + 1
            else:
                chungus = kms - 1
        return -1                
                