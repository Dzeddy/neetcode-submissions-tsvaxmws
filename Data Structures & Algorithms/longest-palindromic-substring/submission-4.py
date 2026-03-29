class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 2:
            return s if s == s[::-1] else s[0]
        st = ""
        stl = 0

        for i in range(len(s)):
            temp = ""
            tl = 0
            l , r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print(l, r)
                temp = s[l:r + 1]
                tl = len(temp)
                if tl > stl:
                    st = temp
                    stl = tl
                l -= 1
                r += 1
            l , r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp = s[l:r + 1]
                tl = len(temp)
                if tl > stl:
                    st = temp
                    stl = tl
                l -= 1
                r += 1
        return st