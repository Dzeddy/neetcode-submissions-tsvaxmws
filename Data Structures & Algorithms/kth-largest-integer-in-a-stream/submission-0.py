def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return l

class KthLargest:
    def __init__(self, k: int, nums):
        self.nums = []
        self.k = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
        else:
            idx = binary_search(self.nums, val)
            self.nums.insert(idx, val)
        if len(self.nums) > self.k:
            self.nums.pop(0)
        return self.nums[0]