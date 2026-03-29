class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []

        res = []

        def dfs(i):
            if sum(path) > target:
                return
                
            if sum(path) == target:
                res.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j)
                path.pop()
        
        dfs(0)

        return res