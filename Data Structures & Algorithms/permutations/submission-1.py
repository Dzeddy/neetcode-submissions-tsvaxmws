class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        path = []

        taken = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())

            for i in range(len(nums)):
                if taken[i]:
                    continue

                taken[i] = True

                path.append(nums[i])

                backtrack()

                path.pop()

                taken[i] = False

            
        backtrack()

        return res