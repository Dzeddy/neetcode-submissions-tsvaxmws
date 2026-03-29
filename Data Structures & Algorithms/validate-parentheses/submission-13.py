class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapp = {']' : '[', '}' : '{', ')' : '('}

        for i in s:
            if i in mapp:
                if not stack:
                    return False
                else:
                    tmp = stack.pop()
                    if tmp != mapp[i]:
                        return False
            else:
                stack.append(i)

        if stack:
            return False

        return True