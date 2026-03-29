def twoSum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1
    sett = set()
    while l < r:
        summ = numbers[l] + numbers[r]
        if summ == target:
            print(target, numbers[l], numbers[r])
            sett.add(tuple(sorted([-target,numbers[l],numbers[r]])))
            l += 1
            r -= 1
        if summ < target:
            l += 1
        elif summ > target:
            r -= 1
    print(sett)
    return sett

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store in tuples, make sure they're ordered, use that
        # run 2-sum using an index as target
        # first sort nums
        nums.sort()
        sett = set()
        for i in range(len(nums)):
            sett = sett.union(twoSum(nums[:i] + nums[i + 1:], -nums[i]))
        fin = list(sett)
        return fin