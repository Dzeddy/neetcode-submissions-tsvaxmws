class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # iterate through temperatures
        # 2 stack solution, each stack stores temp and idx
        stack = []
        res = [0 for _ in range(len(temperatures))]
        # we want to store (idx, val) pairs here
        for i in range(len(temperatures)):
            curr = temperatures[i]

            while stack and stack[-1][1] < curr:
                idx, _ = stack.pop()

                res[idx] = i - idx
            
            stack.append((i, curr))
        
        return res

