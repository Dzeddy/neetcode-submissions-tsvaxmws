class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        r = 0 

        mapp = {}
        
        maxx = min(1, len(s))

        while r < len(s):
            if s[r] in mapp:
                l = max(mapp[s[r]] + 1, l)
            mapp[s[r]] = r
            print(l, r)
            maxx = max(maxx, r - l + 1)
            r += 1
        return maxx

