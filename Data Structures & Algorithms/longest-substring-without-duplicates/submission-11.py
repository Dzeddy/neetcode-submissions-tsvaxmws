class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        mapp = {}
        dupes = 0
        # above is the "state"
        l = 0
        best = 0

        for right, char in enumerate(s):
            mapp[char] = mapp.get(char, 0) + 1
            if mapp[char] == 2:
                dupes += 1

            while dupes > 0:
                c = s[l]
                mapp[c] -= 1
                if mapp[c] == 1:
                    dupes -= 1
                l += 1
        
            best = max(best, right - l + 1)
        
        return best