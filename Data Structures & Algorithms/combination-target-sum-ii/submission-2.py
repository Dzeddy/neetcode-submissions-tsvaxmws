class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        path = []

        def dfs(i, total):
            if total == target:
                res.append(path.copy())

            if total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])

                dfs(j + 1, total + candidates[j])

                path.pop()

        dfs(0,0)

        return res