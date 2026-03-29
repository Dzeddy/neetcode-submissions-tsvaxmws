class Solution:
    def isPalindrome(self, s: str) -> bool:
        beg = 0
        s = "".join([v for v in s if v.isalnum()])
        end = len(s) - 1
        if not s:
            return True
        while beg < end:
            if s[beg].lower() != s[end].lower():
                return False
            beg += 1
            end -= 1
        return True