class Solution:
    def tribonacci(self, n: int) -> int:
        T0 = 0
        T1 = 1
        T2 = 1
        arr = [0,1,1]
        if n < 3:
            return arr[n]
        n -= 2
        for i in range(n):
            curr = T0 + T1 + T2
            T0 = T1
            T1 = T2
            T2 = curr
        return curr
            