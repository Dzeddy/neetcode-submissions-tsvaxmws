class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        tina = []

        chi = []

        taken = [False] * len(nums)

        def mhcdd():
            if len(chi) == len(nums):
                tina.append(chi.copy())
                return
            
            for i in range(len(nums)):
                if taken[i]:
                    continue
                taken[i] = True

                chi.append(nums[i])

                mhcdd()

                chi.pop()

                taken[i] = False
            
        mhcdd()

        return tina