class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        sett = set(["+","-","*","/"])

        def eval(l, r, sign):
            if sign == "+":
                return l + r
            elif sign == "-":
                return l - r
            elif sign == "*":
                return l * r
            elif sign == "/":
                return int(l / r)

        for i in range(len(tokens)):
            print(stack)
            if tokens[i] in sett:
                r = stack.pop()
                l = stack.pop()

                res = eval(l, r, tokens[i])

                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]