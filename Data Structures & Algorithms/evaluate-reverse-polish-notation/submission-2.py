def turn_str_to_op(s, A, B):
    match s:
        case "+":
            return A + B
        case "*":
            return A * B
        case "-":
            return A - B
        case "/": 
            return int(A / B)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+","*","-","/"])
        for i in range(len(tokens)):
            if tokens[i] in ops:
                B = stack.pop()
                A = stack.pop()
                stack.append(turn_str_to_op(tokens[i], A, B))
            else:
                stack.append(int(tokens[i]))
        return int(stack[0])