class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        while i < len(nums):
            curr = nums[i]

            if curr == val:
                nums.pop(i)
                continue
            
            i += 1
        
        return len(nums)