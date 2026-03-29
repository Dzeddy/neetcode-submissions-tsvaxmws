class Solution:
    def trap(self, height: List[int]) -> int:
        # discard gaps if there's no wall to the left / to the right
        # track highest wall until current point
        # track 0 
        if not height:
            return 0
        l = 0
        r = 0
        curr_left_height = height[0]
        valley_arr = []
        water = 0
        while r < len(height) - 1:
            r += 1
            # print(l, r)
            if height[r] >= curr_left_height:
                count = 0
                for i in valley_arr:
                    trapped_water = curr_left_height - i
                    count += trapped_water
                l = r
                water += count
                curr_left_height = height[l]
                valley_arr = []
            else:
                valley_arr += [height[r]]
        curr_right_height = 0
        valley_arr = []
        while r >= l:
            print(water)
            print(l, r)
            print(curr_right_height)
            if height[r] >= curr_right_height:
                print(valley_arr)
                count = 0
                for i in valley_arr:
                    trapped_water = curr_right_height - i
                    count += trapped_water
                curr_right_height = height[r]
                water += count
                valley_arr = []
            else:
                valley_arr += [height[r]]
            r -= 1
        return water
            
