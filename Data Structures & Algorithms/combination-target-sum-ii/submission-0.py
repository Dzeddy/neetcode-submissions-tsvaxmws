class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()

        candidates.sort()

        path = []

        def dfs(i, total):
            if total == target:
                res.add(tuple(path.copy()))

            for j in range(i, len(candidates)):
                path.append(candidates[j])

                dfs(j + 1, total + candidates[j])

                path.pop()

        dfs(0,0)

        listres = list([list(i) for i in res])

        return listres