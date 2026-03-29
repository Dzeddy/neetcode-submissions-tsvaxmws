class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        summ = 0
        misf = 10**9
        while r < len(nums):
            summ += nums[r]

            if summ >= target:
                while summ >= target:
                    misf = min(misf, r - l + 1)
                    summ -= nums[l]
                    l += 1
        
            r += 1
        
        return misf if misf < 10**9 else 0