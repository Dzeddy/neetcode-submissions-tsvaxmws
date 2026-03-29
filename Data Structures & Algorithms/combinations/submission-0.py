class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        mask = [0] * n
        path = []
        res = []
        def bt(i):
            if len(path) == k:
                res.append(path.copy())
                return
            
            for j in range(i, n):
                path.append(j + 1)
                bt(j + 1)
                path.pop()

        bt(0)

        return res