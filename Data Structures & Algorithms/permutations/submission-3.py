class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        path = []

        taken = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if taken[i]:
                    continue
                
                taken[i] = True

                path.append(nums[i])

                dfs()

                taken[i] = False

                path.pop()

        dfs()

        return res
