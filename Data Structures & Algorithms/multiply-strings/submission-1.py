class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def char_to_int(c):
            return int(c)

        res = 0

        for idx, i in enumerate(num1):
            for jdx, j in enumerate(num2):
                summ = char_to_int(i) * (10**(len(num1) - idx - 1)) * char_to_int(j) * (10**(len(num2) - jdx - 1))
                res += summ
                
        return str(res)