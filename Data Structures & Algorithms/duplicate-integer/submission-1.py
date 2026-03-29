class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        kek = set()
        for i in nums:
            if i in kek:
                return True
            kek.add(i)
        return False