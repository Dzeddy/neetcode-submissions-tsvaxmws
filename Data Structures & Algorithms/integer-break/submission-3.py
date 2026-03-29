class Solution:
    def integerBreak(self, n: int) -> int:
        maxx = 0

        curr = 1

        msf = defaultdict(int)

        def bt(n, depth):
            nonlocal maxx
            nonlocal curr

            if msf[n] > curr:
                return

            msf[n] = curr

            if depth >= 2:
                maxx = max(curr, maxx)

            for i in range(1, n + 1):
               curr *= i
               
               bt(n - i, depth + 1)

               curr = int(curr / i)
        
        bt(n, 0)

        return maxx

