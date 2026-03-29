class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.lower().replace(" ", "")
        res = ""
        for i in temp:
            if i.isalnum():
                res += i
        print(res)
        print(res[::-1])
        return res == res[::-1]