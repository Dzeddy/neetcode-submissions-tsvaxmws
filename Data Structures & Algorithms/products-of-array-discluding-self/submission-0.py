        # 1 1 1 1 
        # 1 1 2 8 
        # 48 24 6 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        arr1 = [1] * len(nums)
        for i in range(1, len(nums)):
            arr[i] = arr[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            arr1[i] = arr1[i + 1] * nums[i + 1]

        print(list(range(len(nums) - 2, -1, -1)))
        print(arr)
        print(arr1)

        return [arr[i] * arr1[i] for i in range(len(arr))]
            