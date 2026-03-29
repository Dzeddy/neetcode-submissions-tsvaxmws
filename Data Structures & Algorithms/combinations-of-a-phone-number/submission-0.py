class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        path = []
        res = []

        chars = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def dfs(i):
            if i == len(digits):
                if path:
                    res.append("".join(path))
                return

            idx = int(digits[i])

            for j in range(len(chars[idx])):
                path.append(chars[idx][j])
                dfs(i + 1)
                path.pop()

        dfs(0)

        return res