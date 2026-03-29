# [1,2,-3,4]
# [1,2] -3 [4]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        narr = [1] * len(nums)
        arr[0] = nums[0]
        narr[0] = nums[0]
        maximillian = nums[0]
        for i in range(1, len(nums)):
            arr[i] = max(arr[i-1] * nums[i], nums[i])

            narr[i] = narr[i-1] * nums[i]

            arr[i] = max(arr[i], narr[i])

            maximillian = max(arr[i], maximillian)
        negatives = [i for i in narr if i < 0]
        print(arr)
        print(narr)
        negmax = 0
        if negatives:
            nmindex = narr.index(min(narr))
            negdex = negatives.index(min(narr))
            if negatives[:negdex]:
                negmax = max(negatives[:negdex])
        test = int(min(narr) / negmax) if negmax else -10**6
        return max(maximillian, test)