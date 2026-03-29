class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        flag = {}
        flag['empty'] = False
        def dfs(s):
            print(s)
            if s == '':
                flag['empty'] = True
            if s in memo:
                return memo[s]
            for i in range(len(s)):
                if s[:i + 1] in wordDict:
                    dfs(s[i + 1:])
            memo[s] = 1
        dfs(s)
        return flag['empty']