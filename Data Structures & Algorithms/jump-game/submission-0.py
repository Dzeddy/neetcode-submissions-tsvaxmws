class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0

        while curr < len(nums):
            val = nums[curr]

            if curr == len(nums) - 1:
                return True

            if nums[curr] == 0:
                return False

            max_jump = -10**6
            jump_idx = curr

            # goal: reach the furthest jump peeking 2 jumps ahead
            for j in range(curr + 1, min(len(nums), curr + val + 1)):
                jump_r = j + nums[j]
                if jump_r > max_jump:
                    max_jump = jump_r
                    jump_idx = j
            
            if curr == jump_idx:
                return False

            curr = jump_idx
        
        return True


            