class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # 0 1 2 
        arr = [[0] * len(costs[0]) for _ in range(len(costs))] 
        arr[0] = costs[0]
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                color1 = (j + 1) % 3
                color2 = (j + 2) % 3

                arr[i][j] = min(arr[i - 1][color1] + costs[i][j], arr[i - 1][color2] + costs[i][j])
                print(i, j)
                print(arr)
        return min(arr[-1])