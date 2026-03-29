class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        flag = False
        def dfs(s):
            nonlocal flag
            if s == '':
                flag = True
            if s in memo:
                return memo[s]
            for i in range(len(s)):
                if s[:i + 1] in wordDict:
                    dfs(s[i + 1:])
            memo[s] = 1
        dfs(s)
        return flag