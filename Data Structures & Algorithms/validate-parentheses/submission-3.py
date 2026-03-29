class Solution:
    def isValid(self, s: str) -> bool:
        dick = {"{":"}","[":"]","(":")"}
        stack = []
        for i in range(len(s)):
            if s[i] in dick:
                stack.append(dick[s[i]])
            else:
                if not stack or stack.pop() != s[i]:
                    return False
        return True if not stack else False