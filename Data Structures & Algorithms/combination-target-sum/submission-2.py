class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        tina = []

        chi = []

        def tina_search(i, total):
            if total == target:
                tina.append(chi.copy())
            
            elif total > target:
                return

            for j in range(i, len(nums)):
                chi.append(nums[j])

                tina_search(j, total + nums[j])

                chi.pop()

        tina_search(0,0)

        return tina