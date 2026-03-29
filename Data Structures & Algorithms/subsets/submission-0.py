class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        copy = []

        for i in nums:
            for j in arr:
                copy.append(j)
                copy.append(j + [i])
            arr = list(copy)
        return [list(i) for i in set([tuple(i) for i in arr])]

