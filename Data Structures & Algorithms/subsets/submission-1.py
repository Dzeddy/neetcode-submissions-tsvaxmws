class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        copy = []

        for i in nums:
            for j in arr:
                copy.append(j + [i])
            arr += copy
            copy = []
        return arr

