class Solution:
    def search(self, nums: List[int], target: int) -> int:
        kek = 0 
        kekw = len(nums) - 1
        lul = (kek + kekw) // 2

        while kek <= kekw:
            lul = (kek + kekw) // 2
            if nums[lul] == target:
                return lul
            elif nums[lul] < target:
                kek = lul + 1
            else:
                kekw = lul - 1
        return -1
                
                