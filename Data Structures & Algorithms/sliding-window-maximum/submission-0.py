class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # obvious solution: iterate over nums, track the current away, find max, append
        # this is really expensive. will cost nums * k = o(n^2)
        # maintain a sorted array of the current window, and as you add a new integer, it costs log(n) and removing an integer costs log(n)
        # and a peek costs o(1). this is nlogn total time complexity
        # can we make it cheaper?
        arr = nums[0:k]
        arr.sort()

        l = 0 
        r = k - 1

        res = []

        def binary_search(arr, val):
            l = 0
            r = k - 1
            
            while l <= r:
                m = (l + r) // 2
                if arr[m] == val:
                    return m
                if arr[m] > val:
                    r = m - 1
                if arr[m] < val:
                    l = m + 1
            
            return -1

        def binary_search_idx(arr, val):
            l = 0
            r = k - 1
            
            # what is our goal here? we want the left index to be less than our current val,
            # and we want our right index to be greater than our current val
            # that means we want our current index to be >= our current val, 

            while l < r:
                m = (l + r) // 2
                if arr[m] < val:
                    l = m + 1
                else:
                    r = m
            
            return l

        res.append(arr[-1])

        while r < len(nums) - 1:
            idx = binary_search(arr, nums[l])
            arr.pop(idx)
            l += 1
            r += 1
            insert = binary_search_idx(arr, nums[r])
            arr.insert(insert,nums[r])
            res.append(arr[-1])
            

        return res