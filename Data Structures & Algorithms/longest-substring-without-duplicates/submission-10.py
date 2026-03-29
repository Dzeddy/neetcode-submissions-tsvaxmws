class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        # track with hashmap
        mapp = {}

        maximillian = 0

        l = 0
        r = 0

        while r < len(s):
            if s[r] in mapp and mapp[s[r]] >= l:
                maximillian = max(maximillian, r - l)
                l = mapp[s[r]] + 1
                mapp[s[r]] = r
            else:
                maximillian = max(maximillian, r - l + 1)
                mapp[s[r]] = r
            r += 1
        return maximillian