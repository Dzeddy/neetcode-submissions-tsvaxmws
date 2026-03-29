class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for i in s:
            if i in parentheses_map:
                if not stack or stack.pop() != parentheses_map[i]:
                    return False
            else:
                stack.append(i)
        return not stack


            