class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        max_length = len(min(strs, key=lambda x: len(x)))

        for i in range(max_length):
            curr = strs[0][i]

            for string in strs:
                if string[i] != curr:
                    return strs[0][:i]
        
        return strs[0][:max_length]