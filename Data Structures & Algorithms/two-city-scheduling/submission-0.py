class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        rarr = []
        for a, b in costs:
            rarr.append((a - b, a, b))
        rarr.sort()

        print(rarr)
        
        res = 0

        for i in range(len(costs) // 2):
            res += rarr[i][1]
        
        for i in range(len(costs) // 2, len(costs)):
            res += rarr[i][2]

        return res