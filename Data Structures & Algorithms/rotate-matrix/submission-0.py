class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                x = j
                y = i
                count = 0
                temp = matrix[y][x]
                while count < 4:
                    nx, ny = n-y-1, x
                    matrix[ny][nx], temp = temp, matrix[ny][nx]
                    x , y = nx, ny
                    count += 1
                